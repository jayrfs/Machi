#from frames_stitcher import frames_stitcher
import os
import scripts.frames_stitcher

#add paths
inputPath = ".//input//"
outputPath = ".//output//"
extension = ".png"

#get chapter
list_of_files = os.listdir(inputPath)
print(list_of_files)