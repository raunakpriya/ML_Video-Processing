import cv2

## Read
#img = cv2.imread("colorimage.png")
import numpy as np
cap = cv2.VideoCapture(0)

while(1):

	ret,frame = cap.read()
## convert to hsv
	img = frame
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## mask of green (36,0,0) ~ (70, 255,255)
	mask1 = cv2.inRange(hsv, (136,87,111), (180, 255,255))

## mask o yellow (15,0,0) ~ (36, 255, 255)
	mask2 = cv2.inRange(hsv, (99,115,150), (110, 255, 255))

	mask3 = cv2.inRange(hsv, (22,60,200), (60, 255, 255))

	mask4 = cv2.inRange(hsv, (130,26,51), (150, 255, 230))

	mask5 = cv2.inRange(hsv, (0,0,239), (182, 93, 256))
	
	mask6 = cv2.inRange(hsv, (11,26,51), (33, 255, 230))

	mask7 = cv2.inRange(hsv, (5,140,28), (26, 265, 164))

	mask8 = cv2.inRange(hsv, (0,0,27), (0, 49, 240))

	mask9 = cv2.inRange(hsv, (10,26,102), (25, 255, 230))

	mask10 = cv2.inRange(hsv, (0,48,80), (20, 255, 255))

	mask11 = cv2.inRange(hsv, (0,0,0), (0, 255, 255))

## final mask and masked
	mask = cv2.bitwise_or(mask1, mask2)
	target = cv2.bitwise_and(img,img, mask=mask)
	(_,contours,hierarchy)=cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			
			x,y,w,h = cv2.boundingRect(contour)	
			#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

	(_,contours,hierarchy)=cv2.findContours(mask2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			
			x,y,w,h = cv2.boundingRect(contour)	
			#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

	(_,contours,hierarchy)=cv2.findContours(mask3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			
			x,y,w,h = cv2.boundingRect(contour)	
			#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"green color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

	(_,contours,hierarchy)=cv2.findContours(mask4,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			
			x,y,w,h = cv2.boundingRect(contour)	
			#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"purple color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
	#cv2.imshow("d" , img)

	(_,contours,hierarchy)=cv2.findContours(mask5,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			
			x,y,w,h = cv2.boundingRect(contour)	
			#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"white color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
	#cv2.imshow("d" , img)

	(_,contours,hierarchy)=cv2.findContours(mask6,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			
			x,y,w,h = cv2.boundingRect(contour)	
			#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"yellow color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
	#cv2.imshow("d" , img)

	(_,contours,hierarchy)=cv2.findContours(mask7,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			
			x,y,w,h = cv2.boundingRect(contour)	
			#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"brown color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
	#cv2.imshow("d" , img)

	(_,contours,hierarchy)=cv2.findContours(mask8,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			
			x,y,w,h = cv2.boundingRect(contour)	
			#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"gray color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
	#cv2.imshow("d" , img)

	(_,contours,hierarchy)=cv2.findContours(mask9,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			
			x,y,w,h = cv2.boundingRect(contour)	
			#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"orange color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

	(_,contours,hierarchy)=cv2.findContours(mask9,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			
			x,y,w,h = cv2.boundingRect(contour)	
			#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"skin",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

	
	(_,contours,hierarchy)=cv2.findContours(mask9,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			
			x,y,w,h = cv2.boundingRect(contour)	
			#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"black color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
	cv2.imshow("d" , img)

	

	if cv2.waitKey(10) & 0xff == ord('s'):
		cap.release()
		cv2.destroyAllWindows()
		break
cap.release()
cv2.destroyAllWindows()
