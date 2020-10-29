# export txt for DarkLabel
'''
Input format Class: Conf   (x1: %d   y1: %d  x2: %d  y2: %d )
Output format fn, n[,x1,y1,x2,y2,label]

'''
import re

def count_obj(lines, i):
    obj_num = 0
    obj_data = []
    while 'FPS' not in lines[i] and i < 695:
        for item in classes:
            if item in lines[i]:
                obj_num += 1
                data = [int(s1) for s1 in re.findall('\d+', lines[i])][1:] + [classes.index(item)]
                obj_data += data
        i += 1
    return obj_num, obj_data



file = open(r'D:\Parking_Data\B1\samples\Cam2_drive4_D1.txt', 'r')
# output txt file
convertD1 = open(r'D:\Parking_Data\B1\samples\Cam2_drive4_DL1.txt', 'w+')
classes = ['Vehicle', 'Parked', 'Person']
fn = 0
lines = file.readlines()

for i in range(len(lines)):
    if 'FPS' in lines[i]:
        num, data = count_obj(lines, i+2)
#         if num > 0:
#             print('#', fn, ' ', num, data)
        outline = str(fn) + ',' + str(num)
        for j in data:
            outline += ',' + str(j)
        if num > 0:
            convertD1.write(outline + '\n')
        fn += 1
                
file.close()
convertD1.close()
