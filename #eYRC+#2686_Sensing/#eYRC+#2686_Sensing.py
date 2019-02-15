import numpy as np
import cv2

######TAKE IMAGE###############
img = cv2.imread('test_images/1.jpg')

############################################
def play(img):
        '''
        These values of parameters are found by trail and error 
        We can also find by 
        #red = np.uint8([[[0,0,255]]]) ##red colour Bgr
        #hsv_red = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
        #print hsv_red
        We get [0,255,255]
        For red value hsv 
        To set parameters we take
        #Low_hsv  =[H-10,100,100]
        #High Hsv =[H+10,255,255]
        This way we set the hsv value
        '''

        purple1 = [125,213,190]
        purple2 = [130,216,193] ##HSV VALUE OF PURPLE colour on riffle (190,30,84,<--BGR

        orange1 = [7,206,189]
        orange2 = [10,210,193] ##HSV VALUE OF ORANGE colour on riffle (9,210,193,<--BGR

        ############################################    
        #######processing########
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        ## Convert the parameters into a form that OpenCV can understand
        p1 = np.array(purple1) 
        p2 = np.array(purple2)
        o1 = np.array(orange1)  
        o2 = np.array(orange2)  
        ### Masking image to take detect purple and orange colour of riffle #####
        mask1  = cv2.inRange(hsv, p1, p2)
        mask2  = cv2.inRange(hsv, o1, o2)

        mask_inv1 = cv2.bitwise_not(mask1)  ##inverting image so that it can be used 
        mask_inv2 = cv2.bitwise_not(mask2)  ##for making contours
        ############ Taking contours of purple and orange patches ####
        contours1,hierarchy = cv2.findContours(mask_inv1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contours2,hierarchy = cv2.findContours(mask_inv2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        ### Moments for taking centroid of contour ##
        M = cv2.moments(contours1[2]) ##selecting 2nd contour of every image
        N = cv2.moments(contours2[2]) ##since it gives optimum results
        
        ## Centroid of purple contour i.e 1st coordinate of diagonal
        cx1 = int(M['m10']/M['m00'])
        cy1 = int(M['m01']/M['m00'])
        #print "Centroid = ", cx1, ", ", cy1

        ## Centroid of orange contour i.e 2st coordinate of diagonal
        cx2 = int(N['m10']/N['m00'])
        cy2 = int(N['m01']/N['m00'])
        #print "Centroid = ", cx2, ", ", cy2

        ##### Logic for detection of shot ####
       
        cv2.line(img,(0,60),(770,60),(255,255,255),2)  ##Horizontal line cutting all balloons
        m = float(cy2-cy1)/(cx2-cx1)                   ## Slope of line
        for x in range(0,770):                  ## Trajectory of bullet
                y = float(cy2-m*cx2+m*x)
                y1 = int(y)
                cv2.line(img,(cx2,cy2),(x,y1),(255,255,255),1)
                 
        #### intersection of this Horizontal Line with the  ####
        #### trajectory of bullet will make us detect the   ####
        ####          ballon which would be shot            ####

        x = float((m*cx2-cy2+60)/m) # point of Intersection
        ## If this Point falls in the following range then   ###
        ## Corresponding balloon has heighest Probability to get shot ##
        if (0<x<71):
            letter = "I"
        if (70<x<141):
            letter = "J"
        if (140<x<211):
            letter = "K"
        if (210<x<281):
            letter = "L"
        if (280<x<351):
            letter = "M"
        if (350<x<421):
            letter = "N"
        if (420<x<481):
            letter = "O"
        if (480<x<561):
            letter = "P"
        if (560<x<631):
            letter = "Q"
        if (630<x<701):
            letter = "R"
        if (700<x<771):
           letter = "S"
        cv2.imshow('image1',img)
        return letter

if __name__ == "__main__":
    #checking output for single image
    img = cv2.imread('test_images/1.jpg')
    balloon_letter = play(img)
    print balloon_letter, " balloon in range"
    #checking output for all images
    alpha_list = []
    for file_number in range(1,11):
        file_name = "test_images/"+str(file_number)+".jpg"
        pic = cv2.imread(file_name)
        balloon_letter = play(pic)
        alpha_list.append(balloon_letter)
    print alpha_list
    

cv2.imshow('image1',img)

#######################################3                    




############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################

