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
extension = ".jpg"

def write_output(image, filename="image"):
    os.makedirs(f"{outputPath}{filename}")
    if isinstance(image, np.ndarray)==False:
        for index, stuff in enumerate(image):
            cv2.imwrite(f"{outputPath}//{filename}//{filename}_{index}{extension}",stuff)
    else:
        cv2.imwrite(f"{outputPath}{filename}{extension}",image)
    return

if __name__ == "__main__":
    #test code
    imagelist=[]
    folder=os.listdir(inputPath)
    for file in folder:
        photo = cv2.imread(f"{inputPath}{file}")
        imagelist.append(photo)
    write_output(imagelist)