# -- copy files
from shutil import copyfile

folder = "D:/parking/txt/"
new_label = "D:/parking/copyfile/"

for file in os.listdir(folder):
    filename = folder + file
    if filename.endswith('.txt'):
        copyfile(filename, new_label+file)
