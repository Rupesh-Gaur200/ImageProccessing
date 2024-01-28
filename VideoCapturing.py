# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 14:42:54 2024

@author: RUPESH
"""

import cv2 

cap=cv2.VideoCapture("C:\\Users\\RUPESH\\Pictures\\DSC_9380_Trim.mp4")

while True:
    ret,frames=cap.read()
    frames=cv2.resize(frames,(800,700))
    frames=cv2.imshow("Frames", frames)
    k=cv2.waitKey(25)
    if(k==ord("s")):
        break
cap.release()
cv2.destroyAllWindows()    