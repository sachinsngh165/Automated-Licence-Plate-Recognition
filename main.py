import cv2
import numpy as np
import argparse
import os
import segment
import recognize
from crop_image import crop_Rect
import time



# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True,
    help = "Path to the query image")
args = vars(ap.parse_args())

image_name = args['query']
img = cv2.imread(image_name)



#Resize image 
max_dimension = max(img.shape)
scale = 700.0/max_dimension
#resize it. same width and hieght none since output is 'image'.
img = cv2.resize(img, None, fx=scale, fy=scale)

# Find Most possible Contours from given image
cnts = segment.segment_plate(img)

result = ""
# Find number plate from all the contours and recognise it

for ctr in cnts:

	rect = (cv2.minAreaRect(ctr))
	box = cv2.cv.BoxPoints(rect)
	box = np.int0(box)
	plate = crop_Rect(img,rect,box)


	temp = img.copy()
	cv2.drawContours(temp,[box],0,(0,255,0),2)
	cv2.imshow("processing ", temp)
	cv2.waitKey(5)


# Recognize the number plate from extracted contours
	result = recognize.recognize_plate(plate)

# if number plate is valid print number plate and draw Region
	if len(result) > 5:
		box = np.int0(box)
		cv2.drawContours(img,[box],0,(0,255,0),2)
		print('Detected Licence Plate Number : %s')%format(result)
		break

if len(result) < 5:
	print ' Unable to extract plate area ! '
else:
	cv2.imshow("Detected Number Plate ", img)
	print " ! Press Any Key "
	cv2.waitKey()

cv2.destroyAllWindows()

