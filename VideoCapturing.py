# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 14:42:54 2024

@author: RUPESH
"""
# =============================================================================
# here will are going to Capture a video from the computer storage and displaying it 



# import cv2 
# 
# cap=cv2.VideoCapture("C:\\Users\\RUPESH\\Pictures\\DSC_9380_Trim.mp4")
# 
# while True:
#     ret,frames=cap.read()
#     frames=cv2.resize(frames,(800,700))
#     cv2.imshow("Frames", frames)
#     k=cv2.waitKey(25)
#     if(k==ord("s")):
#         break
# cap.release()
# cv2.destroyAllWindows()    
# =============================================================================


# =============================================================================

#here we are Capturing the video from the user webcam 
# import cv2
# 
# cap=cv2.VideoCapture(0)
# 
# while cap.isOpened():
#     ret, frames=cap.read()
#     frames=cv2.resize(frames,(800,600))
#     cv2.imshow("Frames", frames)
#     k=cv2.waitKey(25)
#     if(k==ord("s")):
#         break
#     
# cap.release()
# cv2.destroyAllWindows()    
# =============================================================================
# =============================================================================
# Videp Capturing and saving 
# import cv2
# 
# cap =cv2.VideoCapture(0)
# 
# fourcc=cv2.VideoWriter_fourcc(*"XVID")

#Study this XVID and all format and research more about video Saving
# 
# 
# output=cv2.VideoWriter("C:\\Users\\RUPESH\\Desktop\\output1.avi",fourcc,20.0,(640,480))
# 
# 
# while cap.isOpened():
#     
#     ret, frames=cap.read()
#     frames=cv2.resize(frames,(600,600))
#     
#     cv2.imshow("Frames", frames)
#     
#     output.write(frames)
#     
#     k=cv2.waitKey(25)
#     if(k==ord("s")):
#         break
#     
# output.release()    
# cap.release()
# cv2.destroyAllWindows()
# 
# 
# =============================================================================






































