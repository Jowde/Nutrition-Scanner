import cv2
import pytesseract
import PIL.Image
import os
from text_convertor import TextConvertor
import info_handler


class PhotoScanner():
    def __init__(self) -> None:
        self.img_counter = 0 
        self.startWindow = False
        self.my_config = r"--psm 4 --oem 3"
    
    def setStartWindow(self):
        self.startWindow = True


#Code below is for taking pictures and scanning
    def startPhotoWindow(self, foodName):
        cam = cv2.VideoCapture(0)

        while self.startWindow:
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
                #prob need to change the way files are saved so they dont overwrite each other when program is closed and ran again 
                img_name = os.path.join("images", f"opencv_frame_{self.img_counter}.png")

                #saves image to images folder
                cv2.imwrite(img_name, frame)

                #prints most recently taken screen shot
                text = pytesseract.image_to_string(PIL.Image.open(img_name), config=self.my_config)
                food_item = TextConvertor(foodName)
                food_item.text_parser(text)
                info_handler.add_item(food_item.create_food_item())

                #sets up for next screenshot
                self.img_counter += 1

        cam.release()
        #cam.destroyAllWindows()









#Testing certain images, change # 'opencv_frame_#' to access different images

"""if __name__ == '__main__':
    text1 = pytesseract.image_to_string(PIL.Image.open(os.path.join("images", "opencv_frame_1.png")), config=my_config)
    text2 = pytesseract.image_to_string(PIL.Image.open(os.path.join("images", "opencv_frame_6.png")), config=my_config)
    text3 = pytesseract.image_to_string(PIL.Image.open(os.path.join("images", "opencv_frame_10.png")), config=my_config)

    print("Jambalaya")
    food_item = TextConvertor('Jambalaya', debug = True)
    food_item.text_parser(text1)
    print(food_item.create_food_item())

    '''
    print("Hot Chocolate")
    text_parser(text2)

    print("Protein Powder")
    text_parser(text3)
    '''
"""
#uncomment when uncommenting picture taking
