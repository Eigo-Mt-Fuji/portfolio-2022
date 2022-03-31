import cv2
import numpy as np

def resize_448_33(src_path, dest_path):
    image_toresize = cv2.imread(src_path, cv2.IMREAD_UNCHANGED)
    height, width = image_toresize.shape[:2]

    width_fixed = 448
    height_fixed = 33

    blank_image = np.zeros((height_fixed, width_fixed, 4), np.uint8)
    blank_image[:,:] = (255,255,255,0)
    image_fixed = blank_image.copy()

    x_offset = (int)((width_fixed - width) / 2)
    print(x_offset)
    y_offset = (int)((height_fixed - height) / 2)
    print(y_offset)
    image_fixed[y_offset:y_offset+height, x_offset:x_offset+width] = image_toresize.copy()

    cv2.imwrite(dest_path, image_fixed)
    return dest_path

resize_448_33('./public/img/course_1_headcopy.png', './public/img/course_1_headcopy_448_33.png')
resize_448_33('./public/img/course_5_headcopy.png', './public/img/course_5_headcopy_448_33.png')
resize_448_33('./public/img/course_7_headcopy.png', './public/img/course_7_headcopy_448_33.png')

