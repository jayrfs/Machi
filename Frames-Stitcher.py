import cv2, os
import numpy as np
method = cv2.TM_SQDIFF_NORMED

#create input and output folders if not present
listFiles = os.listdir(".//")
if "input" not in listFiles:
    os.mkdir("input")
if "output" not in listFiles:
    os.mkdir("output")

#add paths
inputPath = ".//input//"
outputPath = ".//output//"

#get chapter
chapter = int(input(f"Choose chapter to stitch: {os.listdir(inputPath)} :"))
prev_image = long_image = cv2.imread(f"{inputPath}{chapter}_frames/0.jpg")
numberFiles = os.listdir(f"{inputPath}{chapter}_frames/")

#
print(f"{len(numberFiles)} images detected in chapter {chapter}")

count = 0
for img_num in range(len(numberFiles)):
    new_image = cv2.imread(f'{inputPath}{chapter}_frames/{img_num}.jpg')
    prev_image_cropped = prev_image[-500:-1,:]
    # cv2.imshow('output', prev_image_cropped)
    # cv2.waitKey(0)

    result = cv2.matchTemplate(prev_image_cropped, new_image, method)

    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    MPx,MPy = mnLoc
    trows,tcols = prev_image_cropped.shape[:2]

    # cv2.rectangle(new_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
    # cv2.imshow('output',new_image)
    long_image = np.concatenate((long_image, new_image[MPy + trows + 1:,:]), axis=0)
    # cv2.imshow('long img', long_image)
    # cv2.waitKey(0)

    prev_image = new_image
    count+=1
    print(count,end=" ")

cv2.imwrite(f'{outputPath}{chapter}_long.png', long_image)