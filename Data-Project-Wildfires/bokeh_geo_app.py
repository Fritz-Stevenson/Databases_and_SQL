import pandas as pd
from bokeh.plotting import ColumnDataSource, output_file, figure, show
from bokeh.tile_providers import get_provider, CARTODBPOSITRON
from bokeh.models import HoverTool
from pyproj import Transformer





def visualize_fire_geo(year_start, year_stop):
    """
    Creates an interactive application that shows geographical, categorical and statistical data
    about fires in a given year.

    :var year: input a single year for display of annual fire history.

    :returns: Automatically calls show for the app. output html is automatically generated.
    """
    df = pd.read_csv('.\\CSV_Files\\or_historical_wildfires.csv')
    df.dropna(inplace=True)

    def wgs84_to_web_mercator(lon, lat):
        transformer = Transformer.from_crs("epsg:4326", "epsg:3857")
        mercator_list = transformer.transform(lat, lon, errcheck=True)
        return mercator_list

    def fuel_to_color(fuel):
        fuel_dict = {'A':'green', 'B':'teal', 'C':'maroon',
                     'F':'darkslategrey', 'G':'Red', 'H':'Orange',
                     'I':'blue', 'J':'lavender','K':'navy','L':'lime','R':'yellow',
                     'T':'grey', 'U':'brown', 'X':'black'}
        return fuel_dict[fuel]
    df['color'] = df['fuel_model'].apply(fuel_to_color)
    # Narrows scope to year var input.
    df = df.loc[df['fire_year'].isin(range(year_start,year_stop+1))]
    # input variables for to_mercator function.
    lon = list(df['longitude'])
    lat = list(df['latitude'])
    # Creates column determining circle size
    df['marker_size'] = 2 + df['total_acres'] ** (1/3)
    df.drop(['longitude', 'latitude'], axis=1, inplace=True)
    #Converting longitude, latitude data to mercator.
    mercator_data = wgs84_to_web_mercator(lon, lat)
    df['mercator_y'] = mercator_data[0]
    df['mercator_x'] = mercator_data[1]
    #We can now set up the bokeh elements
    output_file('fire_geo_tile.html')
    #Information displayed by the hovertool
    tooltips=[("Date", "@report_date"),
              ("Acres_Burned","@total_acres"),
              ("Fuel Description", "@fuel_descr"),
              ("County", "@county")
              ]
    # Other interactive tools
    select_tools = "box_zoom, poly_select, pan, reset"
    # This retrieves the geographical tile backdrop
    tile_provider = get_provider(CARTODBPOSITRON)
    source = ColumnDataSource(df)
    p = figure(title=f'Oregon Fires between {year_start} and {year_stop}', plot_width=800, plot_height=800,
               x_range=(-13883616.858365921,-12913060.932019735), y_range=(5312341.663847514,5780349.220256351),
               x_axis_type='mercator', y_axis_type='mercator', tools=select_tools)
    p.add_tile(tile_provider)
    p.circle('mercator_y', 'mercator_x', source=source, size='marker_size', color='color')
    p.add_tools(HoverTool(tooltips=tooltips))
    show(p)

