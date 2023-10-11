########################################################################
# Author: Jay Reich
# Date: 10/1/2023
# Info: Converts Steam Workshot files to hopefully the correct version
#           to work outside of steam
#       This program creates a new directory where it is ran, and 
#           it needs to be provided with the correct directory that needs
#           to be converted,
#       NOTE: The original workshop directory should be uneffected.
########################################################################


import os, shutil

# shutil.rmtree("newPack")

# change this path to be to the correct workshop folder
path = "C:\Dev_Stuff\SMF\\211820"

dir_list = os.listdir(path)

# print(dir_list)

# will make a file whereever the script is being run from
os.mkdir("newPack")

for item in dir_list:
    temp_path = path + "\\" + item
    print(temp_path)
    temp_list = os.listdir(temp_path)
    for new_item in temp_list:
        if new_item.endswith(".pak"):
            x = temp_path+"\\"+new_item
            print(x)
            dest = "newPack\\" + item + ".pak"
            print(dest)
            shutil.copyfile(x,dest)