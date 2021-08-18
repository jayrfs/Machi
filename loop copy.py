#from frames_stitcher import frames_stitcher
import os
import time
import cv2
from scripts.frames_splitter import frames_splitter

#log start time
start_time = time.perf_counter()

#add paths
inputPath = ".//input//"
outputPath = ".//output//"
extension = ".png"

#get chapter
list_of_files = os.listdir(inputPath)
print("\n\t\tMachi Image-Stitcher")
print("\nDetected folders in .\input:\n")
print("\t[+] - Input")
print("\t | ")
for files in list_of_files:
    print(f"\t └ {files}")
chapter = (input(f"\nChoose a folder to stitch or press enter to stitch all: "))

if chapter != "":
    try:
        stitchy_code(chapter)
    except:
        print('interation failed! skipping...')
        pass
else:
    for files in list_of_files:
        try:
            image = cv2.imread(f"{inputPath}{files}")
            print(files)
            print(files[:-4])
            frames_splitter(image, files)
        except Exception:
            print('interation failed! skipping...\n'+str(Exception))
            pass

print(f"\nProcess completed in {time.perf_counter()-start_time} seconds.")
input('\nPress ENTER to exit')