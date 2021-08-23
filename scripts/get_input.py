import os, cv2, shutil
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent

def get_input(input_path):
    for element in input_path:
        filename = Path(element).name
        shutil.copy(element, f"{outputPath}\\input\\{filename}")
    return()

#iterate over input path and add objects to new list
input_images=[]
outputPath = get_project_root()