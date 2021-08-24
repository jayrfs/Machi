#from frames_stitcher import frames_stitcher
import os, cv2
from .smart_splitter import smart_splitter
from .write_output import write_output

def smart_split_gui_loop(number=0, prefix="Machi-"):
    #add paths
    inputPath = ".//input//"
    outputPath = ".//output//"
    extension = ".png"

    #get chapter
    list_of_files = os.listdir(inputPath)

    chapter = number

    if chapter != "":
        try:
            photo = cv2.imread(f"{inputPath}{list_of_files[int(chapter)]}")
            split_images = smart_splitter(photo, list_of_files[int(chapter)])
            write_output(split_images[0],prefix)
        except Exception as e:
            print(e)
            pass
    else:
        for files in list_of_files:
            try:
                photo = cv2.imread(f"{inputPath}{files}")
                split_images = smart_splitter(photo, files)
                write_output(split_images[0],prefix)
            except Exception as e:
                print(e)
                pass
    return