import cv2
import numpy as np
method = cv2.TM_SQDIFF_NORMED

def remove_whitespace(image, tolerance=100, scanner_width=100):
    
    #create placeholder image
    final_image = np.zeros((image.shape[0],image.shape[1],image.shape[2]))
    image_height = image.shape[0]
    image_width = image.shape[1]
    image_color = image.shape[2]
    long_long_man = image[0:1, 0:image_width]

    '''if scanner_width == 6969:
        scanner_width = image_width'''

    scanner_center = image_width//2
    scanner_h_start = scanner_center - scanner_width//2
    scanner_h_end = scanner_center + scanner_width//2

    #print(f"scanner center = {scanner_center}\nscanner h start = {scanner_h_start}\nscanner h end = {scanner_h_end}")

    #read template
    whitespace_template = cv2.imread(f'.//resources//whitespace_template.jpg')
    #adjust tolerance
    if tolerance>1:
        whitespace_template_duplicate = whitespace_template
        for i in range(0,tolerance-1):
            whitespace_template = cv2.vconcat([whitespace_template, whitespace_template_duplicate])
    whitespace_template_duplicate = whitespace_template
    for j in range(0,scanner_width-1):
            whitespace_template =cv2.hconcat([whitespace_template, whitespace_template_duplicate])
    #used to dump enlarged_template, do not uncomment
    cv2.imwrite(f".//ignore//dump//templatehaha.jpg", whitespace_template)

    print(f"\nimage height = {image_height}")

    #iterate over every line of the stitched image
    for h_line in range(0, image_height, tolerance):
        crop_image = image[h_line:h_line+tolerance, 0:image_width]
        test_image = image[h_line:h_line+tolerance, scanner_h_start:scanner_h_end]
        #cv2.imwrite(f".//ignore/dele//test{h_line}.png", test_image)
        is_whitespace = np.array_equal(test_image,whitespace_template)
        if is_whitespace == False:
            long_long_man = cv2.vconcat([long_long_man, crop_image])
        #simple check to print progress
        '''percentage_complete = h_line*100/image_height
        if percentage_complete%1==0.0:
            print(f"{percentage_complete}%",end='...')'''

        if h_line%tolerance==0:
            print(f"{h_line}",end='...')
    
    

    '''cv2.imwrite(f".//ignore//dump//output.jpg", long_long_man)
    print(f"image = {image.shape}")
    print(f"final_image = {final_image.shape}")'''
    #np.savetxt("foo.csv", image, delimiter=",")
    #cv2.imshow(long_long_man)
    #cv2.imwrite(f".//trim.png", long_long_man)
    return(long_long_man)

image=remove_whitespace(cv2.imread(f'.//output//74_stitched.png'), 100, 500)
cv2.imwrite(f".//output//74_stitched_trim.png", image)