import cv2
import pytesseract
import PIL.Image
import os

#Uncomment to add image capture
#cam = cv2.VideoCapture(0)

#Uncomment to make the window appear
#cv2.namedWindow("Python Webcam")

img_counter = 0

#set psm to 1, 3, or 4 for text that will be in a block format
#set psm to 11 or 12 to get single text line by line
#Dont touch oem 
my_config = r"--psm 4 --oem 3"


#Code below is for taking pictures and scanning

"""while True:
    #reads camera frame
    ret, frame = cam.read()

    #Checks if frame is readable
    if not ret:
        print('failed to grab frame')
        break
    cv2.imshow('test', frame)

    #Gets key press
    k = cv2.waitKey(1)

    #if Key press is escape
    if k % 256 == 27:
        print("Escape hit")
        break
    #if key press is space
    elif k % 256 == 32:
        img_name = os.path.join("images", f"opencv_frame_{img_counter}.png")

        #saves image to images folder
        cv2.imwrite(img_name, frame)

        print('screenshot')

        #prints most recently taken screen shot
        text = pytesseract.image_to_string(PIL.Image.open(img_name), config=my_config)
        print(text)

        #sets up for next screenshot
        img_counter += 1

"""
#Testing certain images, change # 'opencv_frame_#' to access different images
text1 = pytesseract.image_to_string(PIL.Image.open(os.path.join("images", "opencv_frame_1.png")), config=my_config)
text2 = pytesseract.image_to_string(PIL.Image.open(os.path.join("images", "opencv_frame_6.png")), config=my_config)
text3 = pytesseract.image_to_string(PIL.Image.open(os.path.join("images", "opencv_frame_10.png")), config=my_config)
print("Jambalaya")
print(text1)
print("Hot Chocolate")
print(text2)
print("Protein Powder")
print(text3)

#uncomment when uncommenting picture taking
#cam.release()
#cam.destroyAllWindows()