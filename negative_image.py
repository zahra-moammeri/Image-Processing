import numpy as np
import io
import cv2 as cv

def negative_image(url):
    img = io.imread(url)
    negative_image = 255 - img

    im_c = cv.hconcat([img, negative_image])
    print()
    cv.imwrite('data/dst/opencv_vconcat.jpg', im_c)
    cv.imshow(im_c)
    
    cv.waitKey(0)
    cv.destroyAllWindows()
    return
