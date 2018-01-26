# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import folium 
import pandas

Risk = pandas.read_csv("Risk.txt")

lat = list(Risk["LAT"])
lon = list(Risk["LON"])
ev = list(Risk["ELEV"])

def color_producer(elevation):
    if elevation < 100:
        return 'green'
    elif 100 <= elevation < 300:
        return 'orange'
    else:
        return 'red'
    
map  = folium.Map(location = [45.523, -122.675], tiles="Mapbox Bright",zoom_start=6)

fgv = folium.FeatureGroup(name="RISK")

for lt,ln,el in zip(lat,lon,ev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el)+" m",
        fill_color = color_producer(el), color='grey',fill_opacity=0.7))

map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("Riskmap.html")