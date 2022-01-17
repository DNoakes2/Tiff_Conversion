from tkinter import filedialog
from tkinter import *
from osgeo import gdal
from osgeo.gdalconst import GA_Update
import os, sys
from PIL import Image

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("tiff files","*.tif",),("all files","*.*")))
print (root.filename)

filename = root.filename
ras = gdal.Open(filename, GA_Update)
nodata = 255

# loop through the image bands
for i in range(1, ras.RasterCount + 1):
    # set the nodata value of the band
    ras.GetRasterBand(i).SetNoDataValue(nodata)

# unlink the file object and save the results
ras = None

#JP2ECW
outfile = filename[:-3] + "jpg"
im = Image.open(filename)
print ("new filename : " + outfile)
out = im.convert("RGB")
out.save(outfile, "JPEG", quality=200)
