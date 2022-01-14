from osgeo import gdal
import os

tiffPath = os.getcwd()
dataset = gdal.Open(tiffPath, gdal.GA_ReadOnly)
for x in range(1, dataset.RasterCount + 1):
    band = dataset.GetRasterBand(x)
    array = band.ReadAsArray()
