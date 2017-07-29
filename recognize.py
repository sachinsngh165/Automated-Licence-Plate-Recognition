from PIL import Image
import pyocr
import cv2

def recognize_plate(plate):


	# Converting color image to grayscale image
    grayscale = cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY)
    
    
    # Apply filters to remove noise 
    med_blur = cv2.medianBlur(grayscale,3)
    blur = cv2.GaussianBlur(med_blur,(3,3),0)
    
     # Convert image to binary image
    _, bin_img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)


    image = Image.fromarray(bin_img)
 
    
   
    
# Get all the ocr tools available
    tools = pyocr.get_available_tools()
    tool = tools[0]

# Apply recognizing tool to extracted number plate
    plate_number = tool.image_to_string( image, lang='eng', builder=pyocr.builders.DigitBuilder() )
    return plate_number