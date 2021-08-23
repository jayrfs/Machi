import os, cv2

#iterate over input path and add objects to new list
input_images=[]

def get_input(input_path):
    for element in input_path:
        input_images.append(cv2.imread(element))
    print(len(input_images))
    return(input_images)
        