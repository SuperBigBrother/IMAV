import cv2
import numpy as np
Maxval = 20000
Minval = 10000
x_weight = 0
y_weight = 0
weight = 0
cap=cv2.VideoCapture(0)
while(1):
# 获取每一帧
    frame = cv2.imread('/Users/Xavier/Desktop/1.png')
# 转换到 HSV
    blur = cv2.GaussianBlur(frame,(5,5),0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
# 设定蓝色的阈值
    lower_blue=np.array([20,100,20])
    upper_blue=np.array([220,255,220])
# 根据阈值构建掩模
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
# 对原图像和掩模进行位运算
    res=cv2.bitwise_and(frame,frame,mask=mask)
    blur = cv2.GaussianBlur(res,(5,5),0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    ret,thresh1=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    image, contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        epsilon = 0.1*cv2.arcLength(contour,True)
        approx = cv2.approxPolyDP(contour,epsilon,True)
        if cv2.contourArea(contour) >= Minval :
            if cv2.contourArea(contour) <= Maxval :
                cv2.drawContours(blur, contour, -1, (255,0,0), 3)
                M = cv2.moments(contour)
                x_weight = x_weight + int(M['m10'])
                y_weight = y_weight + int(M['m01'])
                weight = weight + int(M['m00'])
    centroid_x = int(x_weight/weight)
    centroid_y = int(y_weight/weight)
    cv2.circle(blur,(centroid_x,centroid_y), 10, (0,0,255), -1)
# 显示图像
    cv2.imshow('final',blur)
    if cv2.waitKey(1) & 0xFF == ord('q'):break
# 关闭窗口
cv2.destroyAllWindows()

