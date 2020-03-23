import cv2
import numpy as np

img1 = cv2.imread("images/test1.jpeg")
img2 = cv2.imread("images/test2.jpeg")

def compare_images(imageA,imageB):
    if imageA.shape == imageB.shape:
        print("same shape and channels")
        difference = cv2.subtract(imageA,imageB)
        b,g,r = cv2.split(difference)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("Images are completely equal")
        else:
            print("images are different")
    else:
        print("images are different")




compare_images(img1,img2)



