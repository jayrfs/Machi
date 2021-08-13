import cv2
import numpy as np
method = cv2.TM_SQDIFF_NORMED

# for i in range(0, 500):

im1 = cv2.imread(f'frames/58_frames/{10}.png')
# im2 = cv2.imread('frames/58_frames/1.png')

im1_grap = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
# cv2.imshow("output" , im1)
# cv2.waitKey(0)

MAX_FEATURES = 100
orb = cv2.ORB_create(MAX_FEATURES)
keypoints1, descriptors1 = orb.detectAndCompute(im1_grap, None)
print(len(keypoints1))

im1_display = cv2.drawKeypoints(im1, keypoints1, outImage= np.array([]), color=(255,0,0))
cv2.imshow("output" , im1_display)
cv2.waitKey(0)