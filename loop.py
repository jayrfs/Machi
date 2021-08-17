#from frames_stitcher import frames_stitcher
import os
from scripts.frames_stitcher import stitchy_code

#add paths
inputPath = ".//input//"
outputPath = ".//output//"
extension = ".png"

#get chapter
list_of_files = os.listdir(inputPath)
print("\n\t\tMachi Image-Stitcher")
print("\nDetected files in .\input:\n")
print("\t[+] - Input")
print("\t | ")
for files in list_of_files:
    print(f"\t └ {files}")
chapter = (input(f"\nChoose chapter to stitch or press enter to stitch all:"))
print("\n")

if chapter != "":
    stitchy_code(chapter)
else:
    for files in list_of_files:
        stitchy_code(int(files[:2]))
