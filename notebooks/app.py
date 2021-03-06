import panel as pn
import pandas as pd
from diskcache import Cache
import hvplot.pandas
import pathlib

import param
pn.extension("perspective")
pn.config.sizing_mode="stretch_width"

ROOT = pathlib.Path(__file__).parent.parent
cache = Cache(directory=ROOT/".cache")
# cache.clear()
STATIONLIST_CSV = "https://www1.ncdc.noaa.gov/pub/data/noaa/isd-history.csv"

@cache.memoize(name="stationlist", expire=60*60*24, tag='fib')
def read_stationlist():
    print("read")
    return pd.read_csv(STATIONLIST_CSV, parse_dates=["BEGIN", "END"])

STATIONLIST = read_stationlist()
print(STATIONLIST.dtypes)

plot = STATIONLIST.hvplot(x="LAT", y="LON", coastline=True)

class Settings(param.Parameterized):
    clear_cache = param.Event()

    @pn.depends("clear_cache", watch=True)
    def _clear_cache(self):
        print("cache_cleared")
        cache.clear()

settings = Settings()

template = pn.template.FastListTemplate(title="Load Forecast", theme="dark")
template.main.append(pn.pane.Perspective(STATIONLIST, height=500, template="material-dark"))
template.main.append(pn.pane.HoloViews(plot))
template.sidebar.append(pn.Param(settings))
template.servable()