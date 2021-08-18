#from frames_stitcher import frames_stitcher
import os, cv2
import time
from scripts.smart_splitter import smart_splitter
from scripts.write_output import write_output

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
chapter = int((input(f"\nChoose (enter index) a folder to stitch or press enter to stitch all: ")))

if chapter != "":
    try:
        print(f"splitting chapter {chapter}")
        photo = cv2.imread(f"{inputPath}{list_of_files[chapter]}")
        split_images = smart_splitter(photo, list_of_files[chapter])
        write_output(split_images[0],split_images[1])
    except Exception as e:
        print(e)
        pass
else:
    for files in list_of_files:
        try:
            print(f"splitting chapter {chapter}")
            photo = cv2.imread(f"{inputPath}{files}")
            split_images = smart_splitter(photo, files)
            write_output(split_images[0],split_images[1])
        except Exception as e:
            print(e)
            pass

print(f"\nProcess completed in {time.perf_counter()-start_time} seconds.")
input('\nPress ENTER to exit')