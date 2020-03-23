import cv2
from PIL import Image, ImageChops 
import math, operator, functools
import getimage

import requests
from io import BytesIO

net_img1 = "https://rukminim1.flixcart.com/image/800/800/shapewear/z/u/b/mcbl-dermawear-26-original-imae7rrghqzgjyfv.jpeg?q=90"
net_img2 = "https://rukminim1.flixcart.com/image/800/800/shapewear/u/w/g/trbl-dermawear-30-original-imae7rrgh5a4bzzg.jpeg?q=90"
net_img3 = "https://rukminim1.flixcart.com/image/800/800/shapewear/u/w/g/trbl-dermawear-30-original-imae7rrgh5a4bzzg.jpeg?q=90"


# response_a = requests.get(net_img1)
# response_b = requests.get(net_img2)
# img1 = Image.open(BytesIO(response_a.content))
# img2 = Image.open(BytesIO(response_b.content))

def compare_images(imageA_path,imageB_path):

	response_a = requests.get(imageA_path)
	response_b = requests.get(imageB_path)
    #CV2
	imageA = getimage.url_to_image(imageA_path)
	imageB = getimage.url_to_image(imageB_path)

    #PIL
	img1 = Image.open(BytesIO(response_a.content))
	img2 = Image.open(BytesIO(response_b.content))

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


ans = compare_images(net_img3,net_img2)
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



