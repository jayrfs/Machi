import cv2
import numpy as np
method = cv2.TM_SQDIFF_NORMED
chapter = 75
prev_image = long_image = cv2.imread('frames/%d_frames/7.jpg' % chapter)

count = 0
for img_num in range(7,474):
    #695
    new_image = cv2.imread(f'frames/{chapter}_frames/{img_num}.jpg')
    prev_image_cropped = prev_image[-500:-1,:]
    cv2.imshow('output', prev_image_cropped)
    cv2.waitKey(0)

    result = cv2.matchTemplate(prev_image_cropped, new_image, method)

    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    MPx,MPy = mnLoc
    trows,tcols = prev_image_cropped.shape[:2]

    cv2.rectangle(new_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
    cv2.imshow('output',new_image)
    long_image = np.concatenate((long_image, new_image[MPy + trows + 1:,:]), axis=0)
    # cv2.imshow('long img', long_image)
    # cv2.waitKey(0)

    prev_image = new_image
    count+=1
    print(count)

cv2.imwrite(f'{chapter}_long.png', long_image)