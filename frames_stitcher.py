import cv2, os
import numpy as np
from calculate_features import calculate_features
from statistics import median, mean
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

def stitchy_code(chapter_number,buffer_size=500):
    #counters for stitched and skipped pages
    n_skipped,n_stitched=0,0
    detected_features=[10,10,10,10,10,10,10,10,10,10,10]

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

        #  calculate features
        features=calculate_features(new_image,10000)
        print(f"features = {features}")

        #max and min of detected features from last ten images
        features_max_temp = max(detected_features[-10:])
        features_min_temp = min(detected_features[-10:])

        if features not in detected_features and features > 3000:
            print("fresh image, stitching...")
            long_image = np.concatenate((long_image, new_image[MPy + trows + 1:,:]), axis=0)
            n_stitched+=1
        else:
            print("skipping")
            n_skipped+=1
        # cv2.imshow('long img', long_image)
        # cv2.waitKey(0)

        detected_features.append(features)
        
        prev_image = new_image
        count+=1
        print(count,end=" ")

    #assign old filename
    filename = f"{outputPath}{chapter_number}_stitched.png"
        
    #call rename function and write
    rename_old_files(filename)
    cv2.imwrite(f"{filename}", long_image)
    
    #uncomment when running testcode 1
    #cv2.imwrite(f"{filename}_buffer_{buffer_size}.png", long_image)
    print(f"\nno. of stitched images = {n_stitched}\nno. of skipped images = {n_skipped}")
    print(f"median of features = {median(detected_features)}")
    print(f"mean of features = {mean(detected_features)}")
    print(f"long image size = {long_image.shape}")
    print(f" final image = {long_image}")
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


stitchy_code(chapter,500)


'''
#test code 1
for i in range(100,1500,100):
    print(f"buffer size:{i}")
    stitchy_code(74,i)
'''
