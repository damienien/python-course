import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('./img/banane.jpg')
original_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_invert = cv2.bitwise_not(original_img)
img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
def dodge(x, y):
    return cv2.divide(x, 255 - y, scale=250)
plt.axis('off')
final_img = dodge(original_img, img_smoothing)
plt.imshow(final_img, cmap="gray", vmin=200, vmax=255)
cv2.imwrite('sketch.png', final_img)
