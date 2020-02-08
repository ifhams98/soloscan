import numpy
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('/home/thor/Desktop/FYP/img/2.jpg', 0)
img2 = cv2.imread('/home/thor/Desktop/FYP/img/1.jpg', 0)

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

#img1 = cv2.drawKeypoints(img1, kp1, img1)
#img2 = cv2.drawKeypoints(img2, kp2, img2)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des2, des1, k=2)

good_matches = []
for m,n in matches:
	if m.distance < 0.6*n.distance:
		good_matches.append([m])

fimg = cv2.drawMatchesKnn(img2, kp2, img1, kp1, good_matches, None,  flags=2)

plt.imshow(fimg)
plt.show()
cv2.imwrite('home/thor/Desktop/FYP/new_img/hello.jpg', fimg)
