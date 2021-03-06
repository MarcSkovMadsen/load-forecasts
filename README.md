# Load Forecasting Experiments

This project is used to develop simple data pipelines, visualizations, models and apps based on weather and load data.

Checkout the `notebooks/overview.ipynb` on binder

[![Binder Lab](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MarcSkovMadsen/load-forecasts/HEAD?filepath=notebooks%2Foverview.ipynb&urlpath=lab)

Copy markdown link to clipboard

or following the installation instructions below.

## Installation

Using conda

```bash
conda env create -f environment.yml
conda activate load-forecasts
```

## Notebooks

You can now run

```bash
jupyter lab
```

and open the `notebooks/overview.ipynb` notebook.

## App

You can run the app via

```bash
panel serve notebooks/app.py --show
```

## Development

Before you git push please clean the notebooks via

```bash
jupyter nbconvert --clear-output --inplace notebooks/*.ipynb
```

For app development with hot reload use

```bash
panel serve notebooks/app.py --auto --show
```