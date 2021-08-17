import cv2, os
import numpy as np
from remove_whitespace import remove_whitespace
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
extension = ".png"

#get chapter
chapter = int(input(f"Choose chapter to stitch: {os.listdir(inputPath)} :"))


def stitchy_code(chapter_number,buffer_size=300):

    numberFiles = os.listdir(f"{inputPath}{chapter_number}_frames/")
    prev_image = long_image = cv2.imread(f"{inputPath}{chapter_number}_frames/0.jpg")
    count = 0
    
    print(f"{len(numberFiles)} images detected in chapter {chapter_number}")
    for img_num in range(len(numberFiles)):
        new_image = cv2.imread(f'{inputPath}{chapter_number}_frames/{img_num}.jpg')
        prev_image_cropped = prev_image[-buffer_size:-1,:]
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

    #assign old filename
    filename = f"{outputPath}{chapter_number}_stitched"
        
    #call rename function and write
    #rename_old_files(filename)
    cv2.imwrite(f"{filename}{extension}", long_image)
    
    trimmed_long_image = remove_whitespace(long_image, 20, 50)
    cv2.imwrite(f"{filename}_trim{extension}", trimmed_long_image)

    #uncomment when running testcode 1
    #cv2.imwrite(f"{filename}_buffer_{buffer_size}.png", long_image)
    return


#safeguard to avoid overwriting files
def rename_old_files(filename_old):
    file_duplicate = 0
    number_files_output = os.listdir(outputPath)
    for file in number_files_output:
        if filename_old[:-4] in filename_old:
            file_duplicate += 1
    if file_duplicate>0:
        os.rename(filename_old,f"{filename_old[:-4]}_old({file_duplicate}).png")
    return


stitchy_code(chapter)


'''
#test code 1
for i in range(100,1500,100):
    print(f"buffer size:{i}")
    stitchy_code(74,i)
'''