# -- rename files
import os

count = 0
# -- folder directory
folder = "D:/Parking_Data/B1/test/"

for file in os.listdir(folder):
    filename = folder + file                    # current names
    newname = 'Cam2_YellowT_' + '0'*(6 - len(str(count))) + str(count)             # new name to change
    if filename.endswith('.txt'):
        os.rename(filename, folder + newname + '.txt')
        
    else:
        os.rename(filename, folder + newname + '.jpg')
        continue    # if .jpg files appear in advance
    count += 1
