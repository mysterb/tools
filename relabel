# -- remove class > 2 from label files

import os

folder = "D:/parking/new_data/Cam"
new_label = "D:/parking/new_label/Cam"
for i in range(17):
    folder_name = folder + str(i) + '/'
    label_folder = new_label + str(i) + '/'
    for file in os.listdir(folder_name):
        old_file = folder_name + file
        new_file = label_folder + file
        
        old = open(old_file, 'r')
        new = open(new_file, 'w+')
        
        lines = old.readlines()
        for line in lines:
            if line[0] < '3':
                new.write(line)
        
        old.close()
        new.close()
