import os

pth = "D:/parking/new_data/"

for i in range(17):
    try:
        os.mkdir(pth+"Cam"+str(i))
    except OSError:
        print("Failed to create folder %s" % (pth+"Cam"+str(i)))
    else:
        print("Created folder %s" % (pth+"Cam"+str(i)))
