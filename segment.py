import cv2


def segment_plate(car):
    
    # Converting color image to grayscale image
    grayscale = cv2.cvtColor(car,cv2.COLOR_BGR2GRAY)
    
    
    # Apply filters to remove noise 
    med_blur = cv2.medianBlur(grayscale,3)
    blur = cv2.GaussianBlur(med_blur,(7,7),0)
    cv2.imshow('blurred image',blur)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    
        #  Contrast Enhancement
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(55,35))
    tophat = cv2.morphologyEx(blur, cv2.MORPH_TOPHAT, kernel)
    cv2.imshow('tophat',tophat)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    
    
        # Convert image to binary image
    _, bin_img = cv2.threshold(tophat,80,255,cv2.THRESH_BINARY)
#     cv2.imshow('binary image',bin_img)
    
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    closed_img = cv2.morphologyEx(bin_img,cv2.MORPH_CLOSE,kernel)
    cv2.imshow('binary closed image',closed_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    
    
    
         # Find Contours in the image
    ctrs,hier = cv2.findContours(closed_img.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        # Take only top 10 contours 
    cnts = sorted(ctrs, key = cv2.contourArea, reverse = True)[:7]
    return cnts
