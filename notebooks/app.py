import panel as pn
import pandas as pd
from diskcache import Cache
import hvplot.pandas
import pathlib
import holoviews as hv

import param
pn.extension("perspective")
pn.config.sizing_mode="stretch_width"

ACCENT_COLOR = "#E1477E"
ROOT = pathlib.Path(__file__).parent.parent
cache = Cache(directory=ROOT/".cache")
# cache.clear()
STATIONLIST_CSV = "https://www1.ncdc.noaa.gov/pub/data/noaa/isd-history.csv"

@cache.memoize(name="stationlist", expire=60*60*24, tag='fib')
def read_stationlist():
    print("read")
    return pd.read_csv(STATIONLIST_CSV, parse_dates=["BEGIN", "END"])

STATIONLIST = read_stationlist()

plot = STATIONLIST.hvplot(x="LON", y="LAT", kind="points", coastline=True, color=ACCENT_COLOR, responsive=True, height=500)
plot = hv.element.tiles.EsriImagery() * plot

class Settings(param.Parameterized):
    clear_cache = param.Event()

    @pn.depends("clear_cache", watch=True)
    def _clear_cache(self):
        print("cache_cleared")
        cache.clear()

settings = Settings()

template = pn.template.FastListTemplate(title="Load Forecast", theme="dark")
template.main.append(pn.Column(pn.pane.Markdown("# Noaa Station List"), pn.pane.HoloViews(plot), pn.widgets.DataFrame(STATIONLIST.head())))
template.sidebar.append(pn.Param(settings))
template.servable()