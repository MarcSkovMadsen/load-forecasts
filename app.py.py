"""


Run this app for development via

```
panel serve 'notebooks/app.py' --auto --show
```
"""
from pandas.core.base import NoNewAttributesMixin
import panel as pn
import pandas as pd
from diskcache import Cache
import geoviews as gv
import geoviews.tile_sources as gvts
import hvplot.pandas
import pathlib
import holoviews as hv
from bokeh import models
import pathlib
import param
from datashader.utils import lnglat_to_meters
from holoviews.streams import RangeXY

pn.extension("perspective")
pn.config.sizing_mode = "stretch_width"

ACCENT_COLOR = "#E1477E"
ROOT = pathlib.Path(__file__).parent.parent
cache = Cache(directory=ROOT / ".cache")
cache.clear()

STATIONLIST_PATH = (
    pathlib.Path(__file__).parent.parent / "data" / "gold" / "noaa_stations" / "isd-history.csv"
)
STATIONLIST_CSV = "https://www1.ncdc.noaa.gov/pub/data/noaa/isd-history.csv"

DISPLAY_COLUMNS = [
    "STATION",
    "CTRY",
    "STATE",
    "BEGIN",
    "END",
    "USAF",
    "WBAN",
    "ICAO",
    "LAT",
    "LON",
    "ELEV(M)",
]


def to_meters(row):
    return lnglat_to_meters(row["LON"], row["LAT"])


def read_stationlist():
    return pd.read_csv(STATIONLIST_PATH, parse_dates=["BEGIN", "END"])


def ingest_station_list():
    stations = (
        pd.read_csv(STATIONLIST_CSV, parse_dates=["BEGIN", "END"])
        .rename(columns={"STATION NAME": "STATION"})
        .sort_values(by=["STATION"])
    )
    xy_in_meters = stations.apply(to_meters, result_type="expand", axis=1)
    stations["X"] = xy_in_meters[0]
    stations["Y"] = xy_in_meters[1]
    STATIONLIST_PATH.parent.mkdir(parents=True, exist_ok=True)
    stations.to_csv(STATIONLIST_PATH, index=False)


if not STATIONLIST_PATH.exists():
    ingest_station_list()
STATIONLIST = read_stationlist()
# STATIONLIST = STATIONLIST.sample(200)
class Settings(param.Parameterized):
    top_stations = param.Integer(10, bounds=(0, 50), label="Sample Size")


settings = Settings()


def get_station_map(stations, tile=gvts.CartoLight):
    hover = models.HoverTool(
        tooltips=[
            ("Station", "@{STATION}"),
            ("Country", "@CTRY"),
            ("LON", "@LON"),
            ("LAT", "@LAT"),
        ]
    )

    points = gv.Points(stations, ["LON", "LAT"], ["STATION", "CTRY",], label="Station",).opts(
        height=500,
        width=500,
        global_extent=False,
        tools=[hover],
        color=ACCENT_COLOR,
        active_tools=["box_zoom", "wheel_zoom"],
        size=4,
    )
    return points * tile


# Layout and connect

template = pn.template.FastListTemplate(title="Load Forecasting - ERCOT", theme="dark")
if "dark" in str(template.theme).lower():
    tile = gvts.CartoMidnight
else:
    tile = gvts.CartoLight

plot = get_station_map(STATIONLIST, tile=tile)

stream = RangeXY(source=plot)
dataframe_label = pn.pane.Markdown()
dataframe_widget = pn.widgets.DataFrame()


@param.depends(
    x=stream.param.x_range, y=stream.param.y_range, top=settings.param.top_stations, watch=True
)
def update_bounds(x=None, y=None, top=None):
    if x and y:
        x_query = (STATIONLIST["X"] >= x[0]) & (STATIONLIST["X"] <= x[1])
        y_query = (STATIONLIST["Y"] >= y[0]) & (STATIONLIST["Y"] <= y[1])
        data = STATIONLIST[x_query & y_query]
    else:
        data = STATIONLIST
    if not top:
        top = 10
    if len(data)>top:
        data = data.sample(top)
    data=data.sort_values("STATION")[DISPLAY_COLUMNS]
    dataframe_widget.value = data
    dataframe_label.object = f"A random sample of {top} stations shown in the map"


update_bounds(top=settings.top_stations)


template.main.append(
    pn.Column(
        pn.pane.Markdown("# Noaa Stations"),
        pn.pane.HoloViews(plot),
        dataframe_label,
        dataframe_widget,
    )
)
template.sidebar.append(pn.Param(settings))
template.servable()
