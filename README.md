# Load Forecasting Experiments

This project is used to develop simple load forecasting models and apps.

- For an introduction to load forecasting see [Introduction to Load Forecasting](https://acadpubl.eu/hub/2018-119-15/3/567.pdf)
- For an introduction to this repo see the 5min video introduction [here](https://youtu.be/1s5qThItIDU).

If you just want to play around with the nodebooks and code you can do so via Binder.

[![Binder Lab](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MarcSkovMadsen/load-forecasts/HEAD?urlpath=lab)

- Panel App: https://mybinder.org/v2/gh/MarcSkovMadsen/load-forecasts/HEAD?urlpath=/panel/app (Does not work currently)

You should start from the `notebooks/overview.ipynb` notebook.

The ERCOT data is proprietary and you would need access to the ERCOT data in order to ingest this data.

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