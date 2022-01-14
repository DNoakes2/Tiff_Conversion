import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal

ds = gdal.Open("dem.tif")
gt = ds.GetGeoTransform()
projection = ds.GetProjection()

band = ds.GetRasterBand(1)
array = band.ReadAsArray()

# plt.figure()
# plt.imshow(array)
binmask = np.where((Array >= np.mean(array)),1,0)

driver = gdal.GetDriverByName("GTiff")
driver.Register()
outds = driver.Create("binmask.tiff", xsize = binmask.shape[1] ysize = binmask.shape[0], bands = 1, eType = gdal.GDT_Int16)

outds.SetGeoTransform()
outds.SetProjection(proj)
outband = outds.GetRasterBand(1)
outband.WriteArray(binmask)
outband.SetNoDataValue(np.nan)
outband.FlushCache()

outband = None
outds = None
