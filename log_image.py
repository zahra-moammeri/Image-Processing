import numpy as np
import io
import cv2 as cv

def log_image (url):

    img = io.imread(url)
  
    c = 255 / np.log(1+ np.max(img))
    log_image = c *(np.log(img + 1))
    log_image = np.array(log_image, dtype = np.uint8)
    im_c = cv.hconcat([img, log_image])
    cv.imwrite('data/dst/opencv_vconcat.jpg', im_c)
    print()
    cv.imshow(im_c)

    cv.waitKey(0)
    cv.destroyAllWindows()

    return
