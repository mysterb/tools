# -- rename files
import os

folder = "D:/Parking_Data/B1/test"
for file in os.listdir(folder):
    filename = folder + '/' + file                   # current names
    newname = folder + '/' + 'Cam7_Red_' + file      # new names
    os.rename(filename, newname)
