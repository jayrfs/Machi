import cv2
import numpy as np
method = cv2.TM_SQDIFF_NORMED

#final_image

def remove_whitespace(image):
    
    final_image = np.zeros((image.shape[0],image.shape[1],image.shape[2]))
    image_height = image.shape[0]
    image_width = image.shape[1]
    image_color = image.shape[2]
    long_long_man = image[0:1, 0:image_width]

    #iterate over every line of the stitched image
    for h_line in range(image_height):
        crop_image = image[h_line:h_line+1, 0:image_width]
        print(h_line)
        long_long_man = cv2.vconcat([long_long_man, crop_image])

    cv2.imwrite(f".//ignore//dump//output.jpg", long_long_man)
    print(f"image = {image.shape}")
    print(f"final_image = {final_image.shape}")
    #np.savetxt("foo.csv", image, delimiter=",")
    return

remove_whitespace(cv2.imread(f'.//input//74_frames//0.jpg'))