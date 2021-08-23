import os, cv2, shutil
from pathlib import Path

#iterate over input path and add objects to new list
input_images=[]
outputPath = ".//output//"

def get_input(input_path):
    for element in input_path:
        print(element)
        filename = Path(element).name
        shutil.copy(element, f"{outputPath}{filename}")
    return()
        
