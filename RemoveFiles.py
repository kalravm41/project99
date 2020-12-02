import time
import os
import shutil
import sys

directory = input(" Write The Full Path Of The Directory To Be Cleaned After Evary 30 Days: ")

listofFiles = os.listdir(directory)
now = time.time()

for file in listofFiles:

    if os.stat(file).st_mtime < now - 7 * 86400:
        if os.path.exists(directory):
            os.remove(os.path.join(directory,file))

    # if os.path.exists(directory) :
    #     print(directory + "  Working On It......")

    # elif os.path.exists(directory) :
    #     print(directory + "  Directory Not Found!!!")    
