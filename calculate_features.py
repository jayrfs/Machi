import cv2
import numpy as np
method = cv2.TM_SQDIFF_NORMED

# for i in range(0, 500):

def calculate_features(image,amount=10000):
    #im1 = cv2.imread(f'frames/58_frames/{10}.png')
    # im2 = cv2.imread('frames/58_frames/1.png')

    im1_grap = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("output" , im1)
    # cv2.waitKey(0)

    MAX_FEATURES = amount
    orb = cv2.ORB_create(MAX_FEATURES)
    keypoints1, descriptors1 = orb.detectAndCompute(im1_grap, None)
    detected_keypoints=len(keypoints1)
    #print(f"detected keypoints = {detected_keypoints}")

    im1_display = cv2.drawKeypoints(image, keypoints1, outImage= np.array([]), color=(255,0,0))
    #cv2.imshow("output" , im1_display)
    cv2.waitKey(0)
    return(detected_keypoints)

#im1 = cv2.imread(f'input/74_frames/10.jpg')