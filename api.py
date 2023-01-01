"""
Usage: show the Google Map with the given longitude and latitude
"""

import pandas as pd
from bokeh.io import show, output_file, save, export_png
from bokeh.plotting import gmap
from bokeh.models import GMapOptions
from bokeh.models import ColumnDataSource

bokeh_width, bokeh_height = 800, 600

df = pd.read_csv('data.csv')
df = df[df['confidence']=='high']
df = df[:5]

lat, lon = df['latitude'][0], df['longitude'][0]

# API Key may expire one day in the future
api_key = "AIzaSyDBF6Tbp-cvsCtbAbrwVJ61u5d4Ei7mEc4"

def plot(lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng, 
                               map_type=map_type, zoom=zoom)
    p = gmap(api_key, gmap_options, title='Google Map API', 
             width=bokeh_width, height=bokeh_height)
    
    source = ColumnDataSource(df)

    center = p.circle('longitude', 'latitude', size=6, alpha=0.8, 
                      color='yellow', source=source)
    show(p)

    return p

p = plot(lat, lon, map_type='satellite', zoom=10)

p.background_fill_color = None
p.border_fill_color = None

export_png(p, filename="plot.png")