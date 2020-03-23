import cv2
from PIL import Image, ImageChops 
import math, operator, functools


img1_path = "images/img1.jpeg"
img2_path = "images/img2.jpeg"



def compare_images(imageA_path,imageB_path):
    #CV2
    imageA = cv2.imread(imageA_path)
    imageB = cv2.imread(imageB_path)

    #PIL
    img1 = Image.open(imageA_path)
    img2 = Image.open(imageB_path)

    # 1) Comparison by CV2 
    if imageA.shape == imageB.shape:
        print("same shape and channels")
        difference = cv2.subtract(imageA,imageB)
        b,g,r = cv2.split(difference)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("Images are completely equal")
            return 0.0
        else:
            print("images are different")
            return rmsdiff(img1,img2)
    else:
        print("images are different")
        return rmsdiff(img1,img2)

        

# 2) Comparison by ImageChops
def rmsdiff(im1, im2):

    diff = ImageChops.difference(im1, im2)
    h = diff.histogram()

    rms = math.sqrt(functools.reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))
    ) / (float(im1.size[0]) * im1.size[1]))

    # calculate rms
    return rms


ans = compare_images(img1_path,img2_path)
print(ans)










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



