import cv2 as cv
import numpy as np
import io
def gamma_img(url):
    
    img = io.imread(url)

    for gamma in [0.1, 0.5, 1, 1.5, 2, 2.5]:
        power_law= np.array(255 * ((img / 255)**gamma), dtype = 'uint8' )
        cv.imwrite('gamma_transformed'+str(gamma)+'.jpg', power_law)
        print('the number of gamma is: ' ,gamma)
        cv.imshow(power_law)

    cv.waitKey(0)
    cv.destroyAllWindows()

    return
