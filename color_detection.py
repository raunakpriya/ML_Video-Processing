# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 04:00:23 2019

@author: HP
"""

import cv2
import numpy as np

#Capturing the frames with webcam(number 0)
cap = cv2.VideoCapture(0)

#Using while loop to drive program for infinite loops
while(1):
    # "frame" will get the next frame in the camera( via cap.)
    # 'ret' will obtain return value from getting the camera frame, either true or false.
    ret, frame = cap.read()
    
    # Using cv2.cvtColor(input_image, flag), here flag will determine the type of conversion. 
    # Converting image from BGR To HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Defining the Range of Red Color
    # This creates a mask of red color
    # Objects found in the frame
    red_lower = np.array([136,87,111],np.uint8)
    red_upper = np.array([180,255,255], np.uint8)
    
    # Defining the range of blue color
    blue_lower = np.array([99,115,150],np.uint8)
    blue_upper = np.array([110,255,255], np.uint8)
    
    # Defining the range of the green color
    green_lower = np.array([22,60,200],np.uint8)
    green_upper = np.array([60,255,255], np.uint8)
    
    
    
    
    # Finding the range of red, blue and green color in the image
    red = cv2.inRange(hsv, red_lower, red_upper)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    green = cv2.inRange(hsv, green_lower, green_upper)
    
    # Morphological transformation, Dilation
    # The kernal slides through the image (as in 2D convolution).
    # A pixel in the original image(either 1 or 0) will be considered 1
    # only if atlest one pixel under the kernel is '1'.
    kernel = np.ones((5,5), "uint8")
    
    # Print Kernel 
    red = cv2.dilate(red, kernel)
    
    # Bitwise -AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask = red)
    blue = cv2.dilate(blue, kernel)
    
    # Bitwise -AND mask and original image
    res1 = cv2.bitwise_and(frame, frame, mask = blue)
    green = cv2.dilate(green, kernel)
    
    # Bitwise -AND mask and original image
    res2 = cv2.bitwise_and(frame, frame, mask = green)
    
  

    # Trackig the Red Color
    (ret, contours,hierchy) = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area>300:
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),2)
            cv2.putText(frame, 'red color', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
        
    # Tracking the blue color
    (ret, contours, hierchy) = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area>300:
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),2)
            cv2.putText(frame, 'blue color', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
    

    # Tracking the green colors
    (ret, contours, hierchy) = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area>300:
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),2)
            cv2.putText(frame, 'Green color', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
    
    # Function used to display the image
    cv2.imshow("color tracking", frame)
    
    # the image window will close on the command 's'
    if cv2.waitKey(10)& 0xff == ord('s'):
        cap.release()
        cv2.destroyAllWindows()
        break

# Release the captured frame
cap.release()

# Destroy all of the HighGUI windows.
cv2.destroyAllWindows()
