import os
import numpy as np
import cv2

strDirIn = 'G:\\Pictures\\03-Nov-16'
strDirOut = 'G:\\Pictures\\03-Nov-16\\x4_cubic'
fileExt = '.JPG'


if not os.path.isdir(strDirOut):
    os.mkdir(strDirOut)

for file in os.listdir(strDirIn):
    if file.endswith(fileExt):
        strImgIn = os.path.join(strDirIn, file)
        print('Processing ' + strImgIn)
        img = cv2.imread(strImgIn)
        imgResized = cv2.resize(img, (0, 0), fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
        strImgOut = os.path.join(strDirOut, file)[:-len(fileExt)] + '_x4_cubic.jpg'
        cv2.imwrite(strImgOut, imgResized)
        # cv2.imshow(strImg + ' X4 Cubic', imgResized)
        # cv2.waitKey()
        # cv2.destroyAllWindows()