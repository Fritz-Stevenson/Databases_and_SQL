import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from bokeh.plotting import output_file, figure, show
from bokeh.tile_providers import get_provider, CARTODBPOSITRON
import numpy as np
from pyproj import Transformer
plt.style.use('seaborn-pastel')

def visualize_yearly_fire_scale():
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,10))
    data = pd.read_csv('.\\CSV_Files\\yearly_analysis.csv')
    data['percent_remainder']= 100 - data['est_percentage_burned']
    x = range(1992, 2016)
    y1 = list(data['sqmi_burned'])
    y2 = list(data['est_percentage_burned'])
    y3 = list(data['percent_remainder'])
    ax[0].bar(x, y1, color='red')
    ax[1].bar(x, [100 for year in range(len(x))], color='red')
    ax[1].bar(x, y3, color='green')
    ax[0].set_title('Square Miles Burned in Oregon Wildfires')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('burn damage(sq mi)')
    ax[0].xaxis.set_minor_locator(AutoMinorLocator())
    ax[1].set_title('Percentage Burned in Oregon Wildfires')
    ax[1].set_xlabel('Year')
    ax[1].set_ylabel('Estimated Percent Burned')
    ax[1].xaxis.set_minor_locator(AutoMinorLocator())
    plt.savefig('or_yearly_fire_scale.png')
    return plt.show()

def visualize_fire_geo(year = 2015):
    output_file('fire_geo_tile.html')
    #df = pd.read_csv('.\\CSV_Files\\yearly_analysis.csv')
    #df = df['longitude', 'latitude']
    #df.dropna(inplace=True)
    #lon = df['Longitude']
    #lat = df['Latitude']
    #mercator_data = wgs84_to_web_mercator(lon, lat)
    tile_provider = get_provider(CARTODBPOSITRON)
    p = figure(x_range=(-13883616.858365921,-12913060.932019735), y_range=(5312341.663847514,5780349.220256351),
               x_axis_type='mercator', y_axis_type='mercator')
    p.add_tile(tile_provider)
    return show(p)

def wgs84_to_web_mercator(lon, lat):
    mercator_list = []
    transformer = Transformer.from_crs("epsg:4326", "epsg:3857")
    for lon, lat in [*zip(lon,lat)]:
        print(lon, lat)
        mercator_list.append(transformer.transform(lon, lat))
    return mercator_list

visualize_yearly_fire_scale()
