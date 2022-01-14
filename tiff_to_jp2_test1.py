#Date: Jan 12th 2021
#Author: Dan Noakes
#About: This code takes a tiff file generated in HEC RAS and converts it into a JP2 file that can be used in CAD or ArcGIS.

import os
from PTL import Image

tiffPath = os.getcwd()
for root, dirs, files in os.walk(tiffPath, topdown=False):
    for name in files:
        print(os.path.join(root, am))
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".tiff":
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jp2"):
                print ("A jp2 file already exists for %s" % name)
            # If a jp2 is *NOT* present, create one from the tiff.
            else:
                outfile = os.path.splitext(os.path.join(root, name))[0] + ".jp2"
                try:
                    im = Image.open(os.path.join(root, name))
                    print ("Generating jp2 for %s" % name)
                    im.thumbnail(im.size)
                    im.save(outfile, "JP2", quality=100)
                except Exception.e:
                    print (e)
