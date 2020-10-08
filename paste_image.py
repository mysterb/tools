# -- paste an image to another
# https://note.nkmk.me/en/python-pillow-paste/

from PIL import Image, ImageDraw, ImageFilter
import os

folder = "D:/Parking_Data/B1/new/"
count = 0
for file in os.listdir(folder):
    filename = folder + file
    if filename.endswith('.jpg'):
        im1 = Image.open(filename)
        clone = im1.copy()
        im2 = Image.open("D:/sample.png")
        
        # specify the position (topleft x, topleft y)
        clone.paste(im2, (273,288))
        clone.save("D:/Parking_Data/B1/test/test_sample"+str(count)+'.jpg')
        count += 1
