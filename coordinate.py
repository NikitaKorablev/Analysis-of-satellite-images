# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 23:55:06 2021

@author: Poly
"""
import rasterio
import pyproj
import glob
# localname = r'D:/other/tress_project/LC08_L1TP_174021_20150608_20170408_01_T1/LC08_L1TP_174021_20150608_20170408_01_T1_B2.TIF'

def coordinate(filepath,lon_min,lat_max):
    # localname = glob.glob(filepath + '*B4.TIF')[0]
    # print('filepath', filepath)
    with rasterio.open(filepath, mode='r') as src:
        dataset = rasterio.open(filepath)
        # Use pyproj to convert point coordinates
        utm = pyproj.Proj(src.crs) # Pass CRS of image from rasterio
        # print('utm',utm)
        lonlat = pyproj.Proj(init='epsg:4326')
        # print('lonlat',lonlat)
    
        lon,lat = (lon_min, lat_max)
        east,north = pyproj.transform(lonlat, utm, lon, lat)
        # print('east,north',east,north)
       
        # What is the corresponding row and column in our image?
        row, col = src.index(east, north) # spatial --> image coordinates
        # print(row,col)
        return(row, col)

# file = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\22-MAY\LC08_L1TP_175021_20180522_20180605_01_T1_'
# a = 56.334723
# b = 43.977427   # ~центр Нижнего

# a = 56.107047
# b = 44.224851



# print(coordinate(file, b, a))






