import cv2, os
import numpy as np

#create input and output folders if not present
listFiles = os.listdir(".//")
if "input" not in listFiles:
    os.mkdir("input")
if "output" not in listFiles:
    os.mkdir("output")

#add paths

def write_output(image, filename="image"):
    inputPath = ".//input//"
    outputPath = ".//output//"
    extension = ".png"

    if isinstance(image, np.ndarray)==False:
        print(len(image))
        for index, stuff in enumerate(image):
            print(index)
            #cv2.imwrite(f"{outputPath}{filename}_{index}_{extension}",stuff)
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