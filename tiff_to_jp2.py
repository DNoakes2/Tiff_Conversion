# Date: Jan 12th 2021
# Author: Dan Noakes
# About: This code takes a tiff file generated in HEC RAS and converts it into a JP2 file that can be used in CAD or ArcGIS.

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
filename = root.filename
root_dir = os.path.dirname(os.path.abspath(__file__)) # This is your project root
in_path = filename #input composite raster


# Exp: The file will be saved into the parent folder of the inputfile #
#---------------------------------------------------------------------#
out_path = root_dir + '/' #output directory for individual bands as files

# Open existing raster file
src_ds = gdal.Open(in_path)

# Scan through the raster bands and configure
for i in range(1,src_ds.RasterCount +1): # Save bands as individual files
    out_ds = gdal.Translate(out_path + 'output' + str(i) + '.jp2', src_ds, format='GTiff', bandList=[i])
    out_ds_name = (out_path + 'output' + str(i) + '.jp2')
    out_ds=None

    ds = gdal.Open(out_ds_name, 1)
    ndv = ds.GetRasterBand(1).GetNoDataValue()
    
    # Set the noValue for entered raster cell value
    # TODO: Request an input from the user to enter a specific value for removing backgroung.
    # E.g.: Please enter the background cell value to set as invisible. The default is "0".


    ## newdv = int(input("Please enter the background cell value to set as invisible. The default is "0": ") or "0")

    newndv = 0
    band1 = ds.GetRasterBand(1).ReadAsArray()
    band1[band1==ndv] = newndv

    ds.GetRasterBand(1).SetNoDataValue(newndv)
    ds.GetRasterBand(1).WriteArray(band1)

## Set up Error Codes for error handling
## Check the link below.
## https://betterprogramming.pub/handling-errors-in-python-9f1b32952423