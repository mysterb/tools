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

        
# -- synthesize B1 Cam 15

'''
syn1 - sample9                                  (570, 180)   51 imgs
syn2 - sample9                                  (570, 260)   50 imgs
syn3 - sample14                                 (510, 240)   45 imgs
syn4 - sample8                                  (470, 193)   46 imgs
syn5 - sample10                                 (-130, 280)  75 imgs
syn6 - sample10,15                   (-130, 280), (570, 170) 75 imgs  
syn7 - sample11                                 (550, 200)   50 imgs
syn8 - sample7,10,13    (140, 290), (60, 280), (600, 160)    75 imgs
syn9 - sample6, bg2                             (540, 230)   50 imgs
'''
from PIL import Image, ImageDraw, ImageFilter
import os

bg = Image.open(r'D:\Parking_Data\B1\samples\Cam15_bg2.jpg')
img1 = Image.open(r'D:\Parking_Data\B1\samples\test.png')
box = (1055,565,1240,790) # left, top, right, bottom
s1 = img1.crop(box)
#s2 = Image.open(r'D:\Parking_Data\B1\sample15.png')
x1, y1 = 540, 150
#x2, y2 = 570 ,170

for i in range(50):
    cone = bg.copy()
    if i > 24:
        for j in range(20,380,10):
            #print(j)
            i1 = s1.rotate(j, expand=True) # rotate sample
            clone = bg.copy()
            #print(x1)
            clone.paste(i1, (x1,y1), i1) # use i1 as foreground
            clone.save(r'D:\Parking_Data\B1\synthesize\syn\20201015_Cam15_syn9_' 
                       +'0'*(6-len(str(i)))+str(i)+'_rotate'+str(j) + '.jpg')
    else:
        cone.paste(s1, (x1,y1), s1)
        cone.save(r'D:\Parking_Data\B1\synthesize\syn\20201015_Cam15_syn9_' +'0'*(6-len(str(i)))+str(i)+'.jpg')

    x1 -= 10
