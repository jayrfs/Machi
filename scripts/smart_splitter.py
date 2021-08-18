import cv2, os
import numpy as np

def smart_splitter(image, name="image", parts=5):

    #var
    image_height = image.shape[0]
    image_width = image.shape[1]
    image_color = image.shape[2]
    part_height = image_height//parts
    cropped_images = []

    print(f"image_height = {image.shape[0]}")
    print(f"image_width = {image.shape[1]}")
    print(f"image_color = {image.shape[2]}")
    print(f"part_height = {image_height//parts}")

    for index, image_part in enumerate(range(0, image_height, part_height)):
        print(index)
        cropped_images.append(image[image_part:image_part+part_height,:])
        if cropped_images[index].shape[0] < part_height/10:
            continue
        cv2.imwrite(f"{str(name)}_{index}.png", cropped_images[index])
    return(cropped_images)

#frames_splitter(cv2.imread("Untitled.png"),100)
smart_splitter(cv2.imread(".//input//71_stitched.png"),"test", 10)