# -- drive a car in Cam 15
from PIL import Image, ImageDraw, ImageFilter
import os

bg = Image.open(r'D:\Parking_Data\B1\samples\Cam15_bg2.jpg')
img = Image.open(r'D:\Parking_Data\B1\samples\test6.png')
pole = Image.open(r'D:\Parking_Data\B1\samples\b_pole.png')

box = (593, 370, 1710, 893)
w, h = 120, 50
x, y = 591, 220
angle = 0
t1 = img.crop(box)
i1 = t1.rotate(-30, expand=True)
# s = t1.resize((w,h), Image.ANTIALIAS)


pbox = (1065, 353, 1194, 554)
pw, ph = 120, 99
px, py = 89, 310
pimg = pole.crop(pbox)
pi = pimg.resize((pw, ph), Image.ANTIALIAS)

for i in range(80):
#     w, h = 120, 40    
    # increasing size
    if i < 3:
        h += 7
    elif i < 6:
        w += 3
    
    # increase to max size
    if i > 10 and i < 23:
        x += 5
        w += 4
        h += 1

        
    x -= 10   
    s = t1.resize((w,h), Image.ANTIALIAS)
    
    # turn 
    if i > 45 and i < 62:
#         s = s.rotate((i-45)*5, expand=True)
        angle += 5
    if i > 59:
        y += 10
        x += 10
        
    clone = bg.copy()
    s = s.rotate(angle, expand=True)
    clone.paste(s, (x,y), s)
    if i > 64:
        clone.paste(pimg, (px, py), pimg)
        
    clone.save(r'D:\Parking_Data\B1\synthesize\syn\20201021_Cam15_drive_' 
                           +'0'*(6-len(str(i)))+str(i)+'.jpg')
print(w, h)
bg.close()
img.close()
