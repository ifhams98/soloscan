import cv2
import numpy as np

for x in range(6):
	img = cv2.imread('/home/thor/Desktop/FYP/img/%s.jpg' %(x))
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	sift = cv2.xfeatures2d.SIFT_create()
	kp1 = sift.detect(img, None)

	img = cv2.drawKeypoints(img, kp1, img)

	cv2.imwrite('/home/thor/Desktop/FYP/1.%s.jpg' %(x), img)
