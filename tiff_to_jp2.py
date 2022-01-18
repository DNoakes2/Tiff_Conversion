#Date: Jan 12th 2021
#Author: Dan Noakes
#About: This code takes a tiff file generated in HEC RAS and converts it into a JP2 file that can be used in CAD or ArcGIS.

import gdal
import numpy as np
from tkinter import filedialog
from tkinter import *
from PIL import Image
import os

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("tiff files","*.tif",),("all files","*.*")))
print (root.filename)
filename = root.filename

root_dir = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
print (root_dir)
in_path = filename #input composite raster
out_path = root_dir + '/' #output directory for individual bands as files

#Open existing raster ds
src_ds = gdal.Open(in_path)

for i in range(1,src_ds.RasterCount +1): #Save bands as individual files
    out_ds = gdal.Translate(out_path + 'output' + str(i) + '.jp2', src_ds, format='GTiff', bandList=[i])
    out_ds_name = (out_path + 'output' + str(i) + '.jp2')
    out_ds=None

    ds = gdal.Open(out_ds_name, 1)
    ndv = ds.GetRasterBand(1).GetNoDataValue()
    newndv = 0
    band1 = ds.GetRasterBand(1).ReadAsArray()
    band1[band1==ndv] = newndv

    ds.GetRasterBand(1).SetNoDataValue(newndv)
    ds.GetRasterBand(1).WriteArray(band1)
    # print (ds.GetRasterBand(1).GetNoDataValue())
