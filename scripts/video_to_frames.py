import cv2
import imagehash
import numpy as np
from skimage.measure import compare_ssim as ssim 

def CaptureFrames(num):
  vidcap = cv2.VideoCapture(f'{num}.mp4')
  success,image = vidcap.read()
  count = 0
  last_img = None


  while success:
    success,image = vidcap.read()
    croped = image[78:994,630:1347]

    cv2.imshow('video', croped)
    if cv2.waitKey(1) == 27:
      exit(0)
    smol_size = tuple(map(lambda x: int(x*0.05) , croped.shape))
    smol = cv2.resize(croped, (smol_size[0], smol_size[1]), interpolation = cv2.INTER_AREA)
    smol_gray = cv2.cvtColor(smol,cv2.COLOR_BGR2GRAY)
    print('Read a new frame: ', success)
    if last_img is not None:
      # breakpoint()
      # this_hash = imagehash.average_hash(croped)
      # last_hash = imagehash.average_hash(last_img)
      
      
      s = ssim(smol_gray,last_img) 
      # difference =  cv2.subtract(croped, last_img)
      # result = not(np.bitwise_xor(croped,last_img).any())
      # result = not np.any(difference)
      # cv2.imshow('video', difference)
      # breakpoint()
      # print(s)
      print(s)
      if s > 0.9 :
        continue
    last_img = smol_gray
    cv2.imwrite("frames/%d_frames/%d.jpg" %( num ,count), croped)     # save frame as JPEG file      
    count += 1

# breakpoint()
# CaptureFrames(71)
# CaptureFrames(73)
# CaptureFrames(74)
# CaptureFrames(75)
# CaptureFrames(76)
# CaptureFrames(77)
# CaptureFrames(78)
CaptureFrames(80)