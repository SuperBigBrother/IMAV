import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
Maxval = 100000
Minval = 1600
while(True):
    x_weight = 0
    y_weight = 0
    weight = 0
    #ret, frame = cap.read()
    frame = cv2.imread("/Users/Xavier/Desktop/data/gatee3.JPG")
    # Create a CLAHE object (Arguments are optional).
    blur_G = cv2.GaussianBlur(frame,(5,5),0)
    #filter
    blur = cv2.bilateralFilter(blur_G,9,75,75)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    lower_blue=np.array([0,0,0])
    upper_blue=np.array([145,125,145])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    mask_inv = cv2.bitwise_not(mask)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    blur = cv2.GaussianBlur(res,(5,5),0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(gray)
    # Filter to 'white' the pillar
    ret,thresh1=cv2.threshold(cl1,105,255,cv2.THRESH_BINARY_INV)
    ret,thresh2=cv2.threshold(cl1,15,255,cv2.THRESH_BINARY_INV)
    thresh = cv2.addWeighted(thresh2,1,thresh1,1,0)
    # Find and Draw contours
    image, contours, hierarchy = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    # Find window
    for contour in contours:
        epsilon = 0.1*cv2.arcLength(contour,True)
        approx = cv2.approxPolyDP(contour,epsilon,True)
        if cv2.contourArea(contour) >= Minval :
            if cv2.contourArea(contour) <= Maxval :
                cv2.drawContours(frame, contour, -1, (255,0,0), 3)
                cv2.drawContours(blur, contour, -1, (255,0,0), 3)
                M = cv2.moments(contour)
                x_weight = x_weight + int(M['m10'])
                y_weight = y_weight + int(M['m01'])
                weight = weight + int(M['m00'])
    if x_weight and y_weight and weight:
        centroid_x = int(x_weight/weight)
        centroid_y = int(y_weight/weight)
        cv2.circle(frame,(centroid_x,centroid_y), 10, (0,0,255), -1)
    cv2.imshow('result 2',thresh2)
    cv2.imshow('result 1',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):break
    if cv2.waitKey(1) = ord('m'):

cap.release()
cv2.destroyAllWindows()


