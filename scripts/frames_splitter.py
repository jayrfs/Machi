import cv2, os
import numpy as np

def unique_count_app(image):
    colors, count = np.unique(image.reshape(-1,image.shape[-1]), axis=0, return_counts=True)
    return colors[count.argmax()]

def frames_splitter(image, name="image", parts=5):

    #var
    image_height = image.shape[0]
    image_width = image.shape[1]
    image_color = image.shape[2]
    part_height = image_height//parts
    cropped_images = []

    for index, image_part in enumerate(range(0, image_height, part_height)):
        print(index)
        print(unique_count_app(image[image_part:image_part+part_height,:]))
        '''cropped_images.append(image[image_part:image_part+part_height,:])
        cv2.imwrite(f"{str(name[:-4])}_{index}.png", cropped_images[index])
'''
        exit()
    return(cropped_images)

#frames_splitter(cv2.imread("Untitled.png"),100)
frames_splitter(cv2.imread(".//input//71_stitched_trim.png"))