from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
import tkinter
import tkinter.filedialog

root = tkinter.Tk()
dirname = tkinter.filedialog.askdirectory(parent=root, initialdir="/",
                                    title='Please select a directory')
fileName = input("Please enter the file path")
ds = gdal.Open(fileName)
array = ds.GetRasterBand(1).ReadAsArray()
plt.imshow(array)
plt.colorbar()


