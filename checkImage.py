import cv2
import numpy as np
from PIL import Image, ImageChops 
import math, operator, functools

# im1 = Image.open("images/mun1.jpg")
# im2 = Image.open("images/mun2.jpg")
img1 = cv2.imread("images/mun1.jpg")
img2 = cv2.imread("images/mun2.jpg")

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
        


def rmsdiff(im1, im2):

    diff = ImageChops.difference(im1, im2)
    h = diff.histogram()

    rms = math.sqrt(functools.reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))
    ) / (float(im1.size[0]) * im1.size[1]))

    # calculate rms
    return rms













# PATENT CODE 
# def similar_images(imageA,imageB):
#     sift = cv2.xfeatures2d.SIFT_create()
#     kp_1, desc_1 = sift.detectAndCompute(imageA, None)
#     kp_2, desc_2 = sift.detectAndCompute(imageB, None)

#     index_params = dict(algorithm=0, trees=5)
#     search_params = dict()
#     flann = cv2.FlannBasedMatcher(index_params, search_params)

#     matches = flann.knnMatch(desc_1, desc_2, k=2)

#     good_points = []
#     ratio = 0.6
#     for m, n in matches:
#         if m.distance < ratio*n.distance:
#             good_points.append(m)
#     print(len(good_points))
#     result = cv2.drawMatches(imageA, kp_1, imageB, kp_2, good_points, None)





# print(rmsdiff(im1,im2))



