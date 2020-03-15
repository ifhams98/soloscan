import numpy as np
import cv2
import matplotlib.pyplot as plt

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((7*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:7].T.reshape(-1,2)

# Arrays to store object points and image points from all the images
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane

im = cv2.imread('/home/thor/Desktop/FYP/camera_calibration/data/5.jpg') #chess board image
# resizing images with ratio 0.25, image size is very large
img = cv2.resize(im, (0, 0), fx=0.35, fy=0.35)

#cv2.imshow('img1', img1) #showing the loaded image
#cv2.waitKey(2000)
#print "in loop"
	
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
#cv2.imshow('gray', gray) #showing the loaded image
#cv2.waitKey(2000)
	
# Find the chess board corners
ret, corners = cv2.findChessboardCorners(gray, (7, 7), None)

# If found, add object points, image points (after refining them)
if ret == True:

    	objpoints.append(objp)

    	corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
    	imgpoints.append(corners2)

    # Draw and display the corners
    	img = cv2.drawChessboardCorners(img, (7, 7), corners2, ret)
	#plt.imshow(img3)
	#plt.savefig('/home/thor/Desktop/FYP/cali_result/img.jpg')
	#plt.imshow(img)
	#plt.savefig('/home/thor/Desktop/FYP/camera_calibration/res/new2.jpg')

	#cv2.imshow('img', img)
    #cv2.imwrite('/home/thor/Desktop/FYP/camera_calibration/res/%s.jpg' %x, img)
    #cv2.waitKey(2000)
    
    #CALIBRATION
        
	retval, cameraMatrix, distCoeffs, rotvecs, transvecs = cv2.calibrateCamera(objpoints,  imgpoints, gray.shape[::-1], None, None)
	
	#UNDISTORTION
    for x in range(0, 29):
        print x
        image1 = cv2.imread('/home/thor/Desktop/FYP/test_data/%s.jpg' %x) #distorted images
        image2 = cv2.resize(image1, (0, 0), fx=0.25, fy=0.25)
        image = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
	
        h, w = image.shape[:2]
        #print h
        #print w

        newcameramtx, roi=cv2.getOptimalNewCameraMatrix(cameraMatrix, distCoeffs, (w, h), 1, (w, h))
        #print cameraMatrix
        #print newcameramtx
        #print roi

	    # undistort using cv2.undistort()
        dst = cv2.undistort(image, cameraMatrix, distCoeffs, None, newcameramtx)
	
	    # crop the image
        x, y, w, h = rois
        dst = dst[y:y+h, x:x+w]
        cv2.imshow('img', dst)
	cv2.waitKey(5000)
        cv2.imwrite('/home/thor/Desktop/FYP/undistortion_result/calibresul%s.jpg' %x, dst)

########################
	# undistort using remapping
	#dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
	# crop the image
	#x, y, w, h = roi
	#dst = dst[y:y+h, x:x+w]
	#cv2.imshow('img', dst)
	#cv2.waitKey(5000)
	#cv2.imwrite('/home/thor/Desktop/FYP/undistortion_result/calibresultnew.jpg', dst)	
