import cv2, os
import numpy as np

def frames_splitter(image, parts=5):

    #var
    image_height = image.shape[0]
    image_width = image.shape[1]
    image_color = image.shape[2]
    part_height = image_height//parts
    cropped_images = {}

    for index, image_part in enumerate(range(0, image_height, part_height)):
        cropped_images[f"part_{index}_"]=image[image_part:image_part+part_height,:]
        #cv2.imwrite(f"{index}.png", cropped_images[index])

    return(cropped_images)

#frames_splitter(cv2.imread("Untitled.png"),100)
#frames_splitter(cv2.imread(".//input//split//71_stitched_trim.png"))