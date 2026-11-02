# Machine Learning for Earth Observation · Apprentissage automatique pour l'observation de la Terre

A complete, open **45-hour university course** (15 sessions × 3 h) that takes students from their first line of Python to
validated land-cover maps and deep learning on satellite imagery. Every session is a Google Colab notebook with a lecture,
a guided lab and automatic feedback checks.

*Un cours universitaire complet et ouvert de **45 heures** (15 séances de 3 h) : de la première ligne de Python jusqu'aux
cartes d'occupation du sol validées et à l'apprentissage profond sur images satellites. Chaque séance est un notebook
Google Colab avec exposé, laboratoire guidé et vérifications automatiques.*

**Instructor / Chargé de cours :** Noé Carème Fouotsa Manfouo, PhD (Operations Research, Stellenbosch University) · [Portfolio](https://noe2019.github.io/DA-Portfolio-Website/)

---

## Learning outcomes · Objectifs

By the end of the course, students can design, run and validate a machine-learning pipeline for satellite imagery:

1. Write structured Python (functions, loops, pandas) for environmental data.
2. Explain remote-sensing physics and compute spectral indices (NDVI, NDWI, NDBI).
3. Handle vector and raster data with correct coordinate systems (GeoPandas, rasterio, xarray).
4. Extract time series and zonal statistics at scale with Google Earth Engine.
5. Train and compare classifiers (random forest, SVM, k-means) to map land cover.
6. Assess maps with good practices (confusion matrix, area estimates with confidence intervals, spatial cross-validation).
7. Apply a pretrained deep-learning model to open EO data and critique its limits.
8. Communicate a reproducible analysis (GitHub, report, Streamlit app) and its ethical implications.

## Schedule · Calendrier

| # | Session (EN / FR) | Content | Notebook | Due |
|---|---|---|---|---|
| 1 | **Earth observation and Python basics**<br>*Observation de la Terre et bases de Python* | Colab, variables, data structures | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/01_python_bases.ipynb) [`01_python_bases`](notebooks/01_python_bases.ipynb) |  |
| 2 | **Control flow and functions**<br>*Structures de contrôle et fonctions* | Loops, conditions, functions, modules | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/02_controle_fonctions.ipynb) [`02_controle_fonctions`](notebooks/02_controle_fonctions.ipynb) | Quiz 1 |
| 3 | **Data analysis with pandas**<br>*Analyse de données avec pandas* | Reading, cleaning and aggregating weather data | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/03_pandas_meteo.ipynb) [`03_pandas_meteo`](notebooks/03_pandas_meteo.ipynb) | Labs 1–3 |
| 4 | **Remote sensing foundations**<br>*Fondements de la télédétection* | Sensors, resolutions, composites, NDVI/NDWI/NDBI | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/04_teledetection_indices.ipynb) [`04_teledetection_indices`](notebooks/04_teledetection_indices.ipynb) |  |
| 5 | **Vector data**<br>*Données vectorielles* | GeoPandas, CRS, spatial joins | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/05_geopandas_vectoriel.ipynb) [`05_geopandas_vectoriel`](notebooks/05_geopandas_vectoriel.ipynb) | Quiz 2 |
| 6 | **Raster data**<br>*Données matricielles* | rasterio, clipping, zonal stats, xarray | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/06_raster_xarray.ipynb) [`06_raster_xarray`](notebooks/06_raster_xarray.ipynb) | Labs 4–6 |
| 7 | **Earth Engine I — rainfall**<br>*Earth Engine I — pluie* | Collections, filters, reducers, CHIRPS | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/07_gee_chirps.ipynb) [`07_gee_chirps`](notebooks/07_gee_chirps.ipynb) |  |
| 8 | **Earth Engine II — population**<br>*Earth Engine II — population* | HRSL zonal sums, export · midterm exam | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/08_gee_hrsl_population.ipynb) [`08_gee_hrsl_population`](notebooks/08_gee_hrsl_population.ipynb) | Exam · proposal |
| 9 | **Machine learning foundations**<br>*Fondements de l'apprentissage automatique* | Overfitting, pipelines, spatial cross-validation | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/09_ml_fondements.ipynb) [`09_ml_fondements`](notebooks/09_ml_fondements.ipynb) |  |
| 10 | **Land-cover classification**<br>*Classification de l'occupation du sol* | Sentinel-2 + WorldCover, RF/CART/SVM, tuning | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/10_classification_occupation_sol.ipynb) [`10_classification_occupation_sol`](notebooks/10_classification_occupation_sol.ipynb) | Labs 7–9 |
| 11 | **Map validation**<br>*Validation des cartes* | Accuracies, area estimation with CI (Olofsson) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/11_validation_cartes.ipynb) [`11_validation_cartes`](notebooks/11_validation_cartes.ipynb) | Quiz 3 |
| 12 | **Change and time series**<br>*Changements et séries temporelles* | NDVI anomalies, drought, k-means, MODIS | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/12_changements_series_temporelles.ipynb) [`12_changements_series_temporelles`](notebooks/12_changements_series_temporelles.ipynb) |  |
| 13 | **Deep learning for EO**<br>*Apprentissage profond pour l'OT* | ResNet-18 transfer learning on EuroSAT | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/13_apprentissage_profond_eurosat.ipynb) [`13_apprentissage_profond_eurosat`](notebooks/13_apprentissage_profond_eurosat.ipynb) | Labs 10–12 |
| 14 | **Reproducibility, ethics, communication**<br>*Reproductibilité, éthique et diffusion* | Git, ethics checklist, Streamlit app | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/noe2019/ML4EO_Bootcamp/blob/main/notebooks/14_diffusion_streamlit.ipynb) [`14_diffusion_streamlit`](notebooks/14_diffusion_streamlit.ipynb) | Progress report |
| 15 | **Project presentations**<br>*Présentations des projets* | Talks and peer feedback | — | Presentation · final report |

## Assessment · Évaluation

| Component | Weight |
|---|---|
| Lab notebooks (4 submissions) | 20% |
| Online quizzes (3) | 15% |
| Midterm practical exam (session 8) | 20% |
| Term project — proposal, progress report, presentation, final report + GitHub | 45% |

## Getting started · Démarrer

**Colab (recommended):** click a badge above. The first cell clones this repository and installs what is missing.

**Local:**
```bash
git clone https://github.com/noe2019/ML4EO_Bootcamp.git
cd ML4EO_Bootcamp
conda env create -f environment.yml && conda activate ml4eo
jupyter lab notebooks/
```

**Google Earth Engine (sessions 7, 8, 10, 12):** since 13 November 2024 Earth Engine requires a Google Cloud project. Register a
free noncommercial project at <https://code.earthengine.google.com/register> and put its ID in the notebook's `EE_PROJECT`.

## Repository structure

```
notebooks/   one notebook per session + ml4eo_data.py (simulated datasets)
data/        small open datasets: NOAA weather, Natural Earth, South African ward boundaries, CHIRPS samples
img/         figures used in the notebooks
```
Instructor solutions are kept outside the public repository (available on request for teaching use).

## What changed since the 2022 bootcamp

The original one-week workshop given at the Department of Economics, Stellenbosch University (Python, remote sensing,
GeoPandas, Earth Engine, Radiant MLHub; January 2022) is preserved
under the Git tag [`bootcamp-2022`](https://github.com/noe2019/ML4EO_Bootcamp/tree/bootcamp-2022). This version:

- restructures the material into a 15-session university course with objectives, labs, checks and assessment;
- updates Earth Engine authentication (Cloud projects), replaces deprecated Landsat Collection 1 with Sentinel-2 SR + Cloud Score+,
  and uses public ESA WorldCover labels instead of private assets;
- replaces Radiant MLHub (closed in 2023) with EuroSAT / TorchGeo and points to Source Cooperative;
- adds new sessions on raster data, ML foundations with spatial cross-validation, map validation and area estimation,
  time series and drought, deep learning, reproducibility and ethics;
- removes hard-coded local paths, duplicates and `nose` tests (unmaintained), and credits all reused material.

## Licence and credits

Course material: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). See [CREDITS.md](CREDITS.md) for the
material reused from Geo-Python (University of Helsinki), the geopandas-tutorial and open datasets.

If you use this course, please cite: *Fouotsa Manfouo, N. C. (2026). Machine Learning for Earth Observation — open course
notebooks. GitHub: noe2019/ML4EO_Bootcamp.*
