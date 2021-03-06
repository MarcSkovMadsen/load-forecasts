import panel as pn
pn.extension("perspective")
import pandas as pd

data = {"b": ['1981 01 01 00   161    28 10173   270    21     0     0     0',
  '1981 01 01 01   111    33 10175   270    21     0     0 -9999',
  '1981 01 01 02   111    39 10183   330    26     0     0 -9999',
  '1981 01 01 03    94    39 10192 -9999     0     0     0 -9999',
  '1981 01 01 04    72    39 10196 -9999     0     0     0 -9999'],
 'a': [1981, 1981, 1981, 1981, 1981],
 }
df=pd.DataFrame(data)

pn.pane.Perspective(df, columns=df.columns).servable()