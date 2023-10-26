import numpy as np
import cv2

img = cv2.imread('./img/banane.jpg')
original_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_invert = cv2.bitwise_not(original_img)
img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
def dodge(x, y):
    return cv2.divide(x, 255 - y, scale=250)
final_img = dodge(original_img, img_smoothing)
cv2.imshow('final_img', final_img)
cv2.imwrite('./img/sketch.png', final_img)

cv2.waitKey()
cv2.destroyAllWindows
