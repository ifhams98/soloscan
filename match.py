import numpy
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('/home/thor/Desktop/FYP/test data/17.jpg', 0)
img2 = cv2.imread('/home/thor/Desktop/FYP/test data/21.jpg', 0)

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

good_matches = []
for m,n in matches:
	if m.distance < 0.75*n.distance:
		good_matches.append([m])

img3 = cv2.drawMatchesKnn(img1, kp1,  img2, kp2, good_matches, None,  flags=2)

plt.imshow(img3), plt.show()

