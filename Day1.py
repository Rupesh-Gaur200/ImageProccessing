# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 13:47:58 2024

@author: RUPESH
"""

import cv2 # importing open cv as cv2 

#Opening and showing an image 
#Image always stored in an array
#Image in this has two types Gray Scale Image(Back and White image,0) and 3-channel Image(Color image,1)
#cv2.imread function take two arguments first is the src of the image and 0 or 1 to to read image as Gray or 3-channel

# =============================================================================
# img1=cv2.imread("C:\\Users\\RUPESH\\Downloads\\profilePhoto.jpg",1)
# img1=cv2.resize(img1,(700,700))
# cv2.imshow("original",img1)
# print(img1)
# 
# # waitkey function is used to wait or give delay 
# cv2.waitKey(5000)
# 
# #destroyAllWindows will destroy all the window
# cv2.destroyAllWindows()
# 
# 
# =============================================================================
#Challenge 1 Take Image from the User and Convert it into Gray Scale and Save it

# Now to rsolve unicode error just put r in front of input
# =============================================================================
# path=input(r"Please paste the Image path : ")
# cv2.flip() function is used to flip image like invert the image left origintation and right origination and take three parameters (0,-1,1)
# img3=cv2.imread(path,0)
# 
# img3=cv2.resize(img3,(700,700))
# 
# cv2.imshow("Converted Image", img3)
# 
# 
# # Now we have to Save the image for that
# 
# k=cv2.waitKey()
# 
# if(k==ord("s")):
#     cv2.imwrite("C:\\Users\\RUPESH\\Desktop\\output.png", img3)
# 
# else :
#   cv2.destroyAllWindows()
# =============================================================================
