import cv2, os
import numpy as np
from alive_progress import alive_bar

def smart_splitter(image, name="image", parts=10):

    #var
    image_height = image.shape[0]
    image_width = image.shape[1]
    image_color = image.shape[2]
    part_height = image_height//parts
    images_crop_heights = []
    cropped_images = []

    #print(f"image_height = {image.shape[0]}")
    #print(f"image_width = {image.shape[1]}")
    #print(f"image_color = {image.shape[2]}")
    #print(f"part_height = {image_height//parts}")

    is_similar_count = []
    crop_heights = {"start":0,"end":0}

    with alive_bar(title=f"Scanning {name}...",bar="bubbles") as bar:
        for index, image_part in enumerate(range(0, image_height, part_height)):
            #print(index)
            #print(f"image_part = {image_part}")

            #strip scanner
            for strip in range(image_part,image_part+1000,20):
                image1 = image[strip:strip+1,:]
                image2 = image[strip+1:strip+2,:]
                #print(f"scan strip {strip}")
                is_similar =image1.shape == image2.shape and not(np.bitwise_xor(image1,image2).any())
                is_similar_count.append(is_similar)
                if is_similar:
                    crop_heights["end"]=strip
                    images_crop_heights.append(crop_heights.copy())
                    crop_heights["start"]=strip
                    #print(f"true strip {strip}")
                    break
        bar()
        #bar.text(f"hahah{name}")
    
    #make last image extend to boundary
    #print(f"last image before {images_crop_heights[-1]}")
    images_crop_heights[-1]["end"]=image_height
    #print(f"last image after {images_crop_heights[-1]}")

    #remove first part
    images_crop_heights.pop(0)
    
    with alive_bar(len(images_crop_heights), title=f"Splitting {name}...", bar="squares") as bar:
        for index, clip in enumerate(images_crop_heights):
            '''print(clip)
            print(index)'''
            current_dict = images_crop_heights[index]
            image_crop = image[current_dict["start"]:current_dict["end"],:]
            cropped_images.append(image_crop)
            bar()
            #bar.text(f"hahah{name}")
            #cv2.imwrite(f"{name}{index}.png",image_crop)

    #print(f"len(images_crop_heigts) {len(images_crop_heights)}")
    return(cropped_images, name)

#frames_splitter(cv2.imread("Untitled.png"),100)
#smart_splitter(cv2.imread(".//input//71_stitched.png"),"test", 6)

