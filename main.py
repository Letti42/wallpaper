import os
import time
from time import sleep


# Seconds in between each frame
delay = 0.07
folder = "nyan_cat"

# Get the list of all files and directories
path = "C:\\Users\\ms_al\\actual project\\background change py\\"+folder
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
import ctypes

i = 0
while True:
    sleep(delay)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(path,dir_list[i]) , 0)
    if i == len(dir_list)-1:
        i = 0
    i+=1





