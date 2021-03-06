# Load Forecasting Experiments

This project is used to develop simple data pipelines, visualizations, models and apps based on weather and load data.

Checkout the `notebooks/overview.ipynb` on binder

[![Binder Lab](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MarcSkovMadsen/load-forecasts/HEAD?filepath=notebooks%2Foverview.ipynb&urlpath=lab)

Copy markdown link to clipboard

or following the installation instructions below.

## Installation

Using python 3.7.6

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install pip==21.0.1
pip install -r requirements.txt
```

## Notebooks

You can now run

```bash
jupyter lab
```

and open the `notebooks/overview.ipynb` notebook.

## Development

Before you git push please clean the notebooks via

```bash
jupyter nbconvert --clear-output --inplace notebooks/*.ipynb
```

## Docker

You can build a local image via

```bash
jupyter-repo2docker .
```