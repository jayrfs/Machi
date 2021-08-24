#from frames_stitcher import frames_stitcher
import os
import time
from .frames_stitcher import stitchy_code


def smart_stitch_gui_loop(number=0, prefix="Machi-"):

    #add paths
    inputPath = ".//input//"
    outputPath = ".//output//"
    extension = ".png"

    #get chapter
    list_of_files = os.listdir(inputPath)
    chapter = number


    if chapter != "":
        try:
            stitchy_code(chapter)
        except:
            print('interation failed! skipping...')
            pass
    else:
        for files in list_of_files:
            try:
                stitchy_code(int(files[:2]))
            except:
                print('interation failed! skipping...')
                pass