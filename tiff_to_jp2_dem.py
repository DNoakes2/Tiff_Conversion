# Date: Jan 12th 2021
# Author: Dan Noakes
# About: This code takes a tiff file generated in HEC RAS and converts it into a JP2 file that can be used in CAD or ArcGIS.

from logging import exception
import gdal
import numpy as np
from tkinter import filedialog
from tkinter import *
from PIL import Image
import os

# Environment Set-up 
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("tiff files","*.tif",),("all files","*.*")))

# Set Variables
in_path = root.filename #input composite raster
root_dir = os.path.dirname(os.path.abspath(__file__)) # This is your project root

# Exp: The file will be saved into the parent folder of the python #
#---------------------------------------------------------------------#
out_path = root_dir + '/' #output directory for individual bands as files
filename = in_path[:-4]
print (filename)

# Open existing raster file
src_ds = gdal.Open(in_path)

# Scan through the raster bands and configure
for i in range(1,src_ds.RasterCount +1): # Save bands as individual files
    pathname = (filename + "" + str(i) + '.jp2')
    out_ds = gdal.Translate(pathname, src_ds, format='GTiff', bandList=[i], options=['COMPRESS=LZW'])
    out_ds_name = (pathname)
    out_ds = None

    ds = gdal.Open(out_ds_name, 1)
    ndv = ds.GetRasterBand(1).GetNoDataValue()
    
    # Set the noValue for entered raster cell value
    newndv = int(input("Please enter the background cell value to set as invisible. The default is '0': ") or "0")
    bandNum = ds.GetRasterBand(1).ReadAsArray()
    bandNum[bandNum==ndv] = newndv

    ds.GetRasterBand(1).SetNoDataValue(newndv)
    ds.GetRasterBand(1).WriteArray(bandNum)
print ("Done")