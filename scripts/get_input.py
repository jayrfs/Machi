#from frames_stitcher import frames_stitcher
import os, cv2
import time

#add paths
inputPath = ".//input//"
outputPath = ".//output//"
extension = ".png"

if chapter != "":
    try:
        photo = cv2.imread(f"{inputPath}{list_of_files[int(chapter)]}")
        split_images = smart_splitter(photo, list_of_files[int(chapter)])
        write_output(split_images[0],split_images[1])
    except Exception as e:
        print(e)
        pass
else:
    for files in list_of_files:
        try:
            photo = cv2.imread(f"{inputPath}{files}")
            split_images = smart_splitter(photo, files)
            write_output(split_images[0],split_images[1])
        except Exception as e:
            print(e)
            pass

print(f"\nProcess completed in {time.perf_counter()-start_time} seconds.")
input('\nPress ENTER to exit')