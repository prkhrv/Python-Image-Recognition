# import the necessary packages
import numpy as np
import urllib.request
import cv2
import ssl
# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
    gcontext = ssl.SSLContext()
    resp = urllib.request.urlopen(url,context=gcontext)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	# return the image
    return image