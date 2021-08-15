import cv2
import numpy as np
method = cv2.TM_SQDIFF_NORMED

def remove_whitespace(image, tolerance=50):
    
    #create placeholder image
    final_image = np.zeros((image.shape[0],image.shape[1],image.shape[2]))
    image_height = image.shape[0]
    image_width = image.shape[1]
    image_color = image.shape[2]
    long_long_man = image[0:1, 0:image_width]
    #read template
    whitespace_template = cv2.imread(f'.//resources//whitespace_template.jpg')
    #adjust tolerance
    if tolerance>1:
        whitespace_template_duplicate = whitespace_template
        for i in range(0,tolerance-1):
            whitespace_template = cv2.vconcat([whitespace_template, whitespace_template_duplicate])
    
    #used to dump enlarged_template, do not uncomment
    # cv2.imwrite(f".//ignore//dump//output.jpg", whitespace_template)


    #iterate over every line of the stitched image
    for h_line in range(image_height):
        crop_image = image[h_line:h_line+1, 0:image_width]
        print(h_line)
        is_whitespace = np.array_equal(crop_image,whitespace_template)
        if is_whitespace == False:
            long_long_man = cv2.vconcat([long_long_man, crop_image])

    cv2.imwrite(f".//ignore//dump//output.jpg", long_long_man)
    print(f"image = {image.shape}")
    print(f"final_image = {final_image.shape}")
    #np.savetxt("foo.csv", image, delimiter=",")
    #cv2.imshow(long_long_man)
    return(long_long_man)

remove_whitespace(cv2.imread(f'.//input//74_frames//0.jpg'))