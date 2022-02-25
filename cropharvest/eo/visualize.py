#import numpy as np
#import torch
#import PIL
import ee
import folium
#from IPython.display import Image
#import pandas as pd
#import geopandas as gpd
#from datetime import datetime, timedelta
#from tqdm import trange
#import seaborn as sns
#import matplotlib.pyplot as plt
#import julian
#import plotly.express as px
#import plotly.graph_objects as go

def add_ee_layer(self, ee_object, vis_params, name):

	try:
		# display ee.Image()
		if isinstance(ee_object, ee.image.Image):
			map_id_dict = ee.Image(ee_object).getMapId(vis_params)
			folium.raster_layers.TileLayer(
			tiles = map_id_dict['tile_fetcher'].url_format,
			attr = 'Google Earth Engine',
			name = name,
			overlay = True,
			control = True
			).add_to(self)
		# display ee.ImageCollection()
		elif isinstance(ee_object, ee.imagecollection.ImageCollection):
			ee_object_new = ee_object.mosaic()
			map_id_dict = ee.Image(ee_object_new).getMapId(vis_params)
			folium.raster_layers.TileLayer(
			tiles = map_id_dict['tile_fetcher'].url_format,
			attr = 'Google Earth Engine',
			name = name,
			overlay = True,
			control = True
			).add_to(self)
		# display ee.Geometry()
		elif isinstance(ee_object, ee.geometry.Geometry):
			folium.GeoJson(
			data = ee_object.getInfo(),
			name = name,
			overlay = True,
			control = True
		).add_to(self)
		# display ee.FeatureCollection()
		elif isinstance(ee_object, ee.featurecollection.FeatureCollection):
			ee_object_new = ee.Image().paint(ee_object, 0, 2)
			map_id_dict = ee.Image(ee_object_new).getMapId(vis_params)
			folium.raster_layers.TileLayer(
			tiles = map_id_dict['tile_fetcher'].url_format,
			attr = 'Google Earth Engine',
			name = name,
			overlay = True,
			control = True
		).add_to(self)

	except:
		print("Could not display {}".format(name))

folium.Map.add_ee_layer = add_ee_layer

def addlayer(eeObject, vizParams, name):
    my_map = folium.Map(location=[45.5236, -122.6750], zoom_start=3, height=500)
    my_map.add_ee_layer(eeObject, visParams, name)
    my_map.add_child(folium.LayerControl())
    display(my_map)
