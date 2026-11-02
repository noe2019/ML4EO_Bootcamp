"""Simulated Earth-observation datasets used in the ML4EO course (sessions 9, 11, 12 and 14).

All data are synthetic but follow realistic Sentinel-2 surface-reflectance values, so that the notebooks run
offline in seconds. Author: N. C. Fouotsa Manfouo. Licence: CC BY-SA 4.0.
"""
import numpy as np
import pandas as pd

BANDS = ["B2", "B3", "B4", "B5", "B6", "B7", "B8", "B11", "B12"]
CLASSES = ["Water", "Tree cover", "Cropland", "Built-up", "Bare soil"]
# mean surface reflectance per class and band (0-1)
MEANS = np.array([
    [0.060, 0.070, 0.050, 0.045, 0.040, 0.035, 0.030, 0.012, 0.008],   # water
    [0.025, 0.050, 0.030, 0.080, 0.220, 0.280, 0.300, 0.150, 0.070],   # tree cover
    [0.040, 0.080, 0.060, 0.120, 0.280, 0.340, 0.380, 0.220, 0.120],   # cropland
    [0.110, 0.120, 0.130, 0.150, 0.170, 0.180, 0.190, 0.260, 0.220],   # built-up
    [0.090, 0.130, 0.170, 0.200, 0.230, 0.250, 0.260, 0.330, 0.280],   # bare soil
])


def add_indices(df):
    """Add NDVI, NDWI and NDBI columns computed from Sentinel-2 bands."""
    df = df.copy()
    df["NDVI"] = (df.B8 - df.B4) / (df.B8 + df.B4)
    df["NDWI"] = (df.B3 - df.B8) / (df.B3 + df.B8)
    df["NDBI"] = (df.B11 - df.B8) / (df.B11 + df.B8)
    return df


def training_polygons(n_polygons=60, pixels_per_polygon=25, seed=0, area_km=20):
    """Pixels sampled inside digitized training polygons.

    Pixels of the same polygon share a polygon-level offset (same field, same soil, same illumination), which mimics the
    spatial autocorrelation of real training data. Returns a DataFrame with x, y (km), polygon id, class and features.
    """
    rng = np.random.default_rng(seed)
    rows = []
    for pid in range(n_polygons):
        cls = pid % len(CLASSES)
        cx, cy = rng.uniform(0, area_km, 2)
        offset = rng.lognormal(0, 0.12, len(BANDS))            # polygon-specific spectral shift
        for _ in range(pixels_per_polygon):
            refl = MEANS[cls] * offset * rng.lognormal(0, 0.05, len(BANDS))
            x, y = cx + rng.normal(0, 0.05), cy + rng.normal(0, 0.05)
            rows.append([x, y, pid, CLASSES[cls], *refl])
    df = pd.DataFrame(rows, columns=["x_km", "y_km", "polygon", "label", *BANDS])
    return add_indices(df)


def ndvi_time_series(n_pixels=300, seed=1):
    """Monthly NDVI (2014-2021) of smallholder and commercial farm pixels, with the 2015-2016 El Niño drought.

    Returns (wide, info): wide = DataFrame (rows = months, columns = pixel ids), info = DataFrame with each pixel's system.
    """
    rng = np.random.default_rng(seed)
    months = pd.date_range("2014-01-01", "2021-12-01", freq="MS")
    m = months.month.to_numpy()
    drought = ((months >= "2015-06-01") & (months <= "2016-06-01")).astype(float)
    system = np.where(rng.random(n_pixels) < 0.5, "Smallholder", "Commercial")
    base = np.where(system == "Commercial", 0.50, 0.42)
    buffer = np.where(system == "Commercial", 0.6, 0.15)      # irrigation buffers commercial farms
    season = 0.18 * np.cos((m - 2) / 12 * 2 * np.pi)
    ndvi = (base[None, :] + season[:, None] - 0.25 * drought[:, None] * (1 - buffer[None, :])
            + rng.normal(0, 0.02, (len(months), n_pixels)))
    wide = pd.DataFrame(ndvi.clip(0.02, 0.95), index=months, columns=[f"px{i:03d}" for i in range(n_pixels)])
    info = pd.DataFrame({"pixel": wide.columns, "system": system})
    return wide, info
