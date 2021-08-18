import cv2, os
import numpy as np

#create input and output folders if not present
listFiles = os.listdir(".//")
if "input" not in listFiles:
    os.mkdir("input")
if "output" not in listFiles:
    os.mkdir("output")

#add paths
inputPath = ".//input//"
outputPath = ".//output//"
extension = ".png"

def write_output(image, filename="image"):
    if isinstance(image, np.ndarray):
        for index, stuff in enumerate(image):
            cv2.imwrite(f"{outputPath}{filename}_{index}_{extension}",stuff)
    else:
        cv2.imwrite(f"{outputPath}{filename}{extension}",image)
    return

if __name__ == "__main__":
    folder=os.listdir(inputPath)
    for file in folder:
        photo = cv2.imread(f"{inputPath}{file}")
        write_output(photo)