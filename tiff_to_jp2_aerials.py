# Date: Jan 12th 2021
# Author: Dan Noakes
# About: This code takes a tiff file generated in HEC RAS and converts it into a JP2 file that can be used in CAD or ArcGIS.

import gdal
import numpy as np
from tkinter import filedialog
from tkinter import *
from PIL import Image
import matplotlib.pyplot as plt
import os

# Environment Set-up 
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("tiff files","*.tif",),("all files","*.*")))

# Set Variables
# filename = root.filename
root_dir = os.path.dirname(os.path.abspath(__file__)) # This is your project root
in_path = root.filename #input composite raster
out_path = root_dir + '/' #output directory for individual bands as files
# filename = in_path[:-4]

# Open existing raster file
src_ds = gdal.Open(in_path)

# out_ds = gdal.Translate(filename + '' + '.jp2', src_ds, format='GTiff', options=['COMPRESS=LZW'])
pathname = (in_path[:-4] + '.jp2')
out_ds = gdal.Translate(pathname, src_ds, format='GTiff', options=['COMPRESS=LZW'])
out_ds_name = (pathname)
out_ds = None

ds = gdal.Open(out_ds_name, 1)
ndv = ds.GetRasterBand(4).GetNoDataValue()

# Set the noValue for entered raster cell value
newndv = int(input("Please enter the background cell value to set as invisible. The default is '255': ") or "255")
bandNum = ds.GetRasterBand(4).ReadAsArray()
bandNum[bandNum==ndv] = newndv

ds.GetRasterBand(4).SetNoDataValue(newndv)
ds.GetRasterBand(4).WriteArray(bandNum)

print("Complete")