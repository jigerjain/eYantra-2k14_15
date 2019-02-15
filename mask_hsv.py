import numpy as np
import cv2
# Initialize camera
img = cv2.imread('1.jpg')
############################################

# Sample Pixel --> A - [213,154,150] , B - [113,154,150]
param1 = [15,180,180]
param2 = [30,255,200]

############################################    
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
## Do the processing
lower = np.array(param1)    ## Convert the parameters into a form that OpenCV can understand
upper = np.array(param2)
mask  = cv2.inRange(hsv, lower, upper)
res   = cv2.bitwise_and(img, img, mask= mask)

green = np.uint8([[[0,150,200 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print hsv_green
###processing####################
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,100,255,0)
mask_inv = cv2.bitwise_not(mask)
contours,hierarchy = cv2.findContours(mask_inv,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print len(contours)

#img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#ret, mask1 = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

cv2.drawContours(img,contours,-1,(0,150,200),5)
##image display
print mask.shape
print gray.shape
cv2.imshow('image2',img)
#cv2.imshow('jiggy2',mask)
#cv2.imshow('image',gray)
#cv2.imshow('jiggy',mask_inv)
#######################################3                    




############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
