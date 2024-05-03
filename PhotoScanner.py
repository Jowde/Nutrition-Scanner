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

MACRO_LIST = ['serving size', 'calories','total fat', 'saturated fat', 'unsaturated fat', 'total carbohydrate',  'dietary fiber','total sugars', 'added sugars', 'protein']

def text_parser(string: str) -> list[int]:
    '''
    parses text created by camera and extracts macro values from it
    '''
    text = string.lower()
    text = text.replace('\n',' ')
    text = ''.join(letter for letter in text if letter.isalnum() or letter == ' ')
    macro_grams_list = []
    for macro in MACRO_LIST:
        grams = grams_per_macro_finder(text, macro)
        macro_grams_list.append(grams)
        print(f'{macro}: {grams}')
    return macro_grams_list
        
        
def grams_per_macro_finder(text: str, macro: str) -> int:
    '''
    checks if an amount in grams can be extract from the photo text 
    If not returns 0 
    '''
    index = text.find(macro)
    spaced_parse = False
    grams = ''
    if index >=0:
        index = index + len(macro)
        while True:
            if text[index].isdigit():
                grams += text[index]
                
            elif not spaced_parse:
                spaced_parse = True
                
            else:
                
                break
            index+=1
            
        if grams =='':
            grams = 0
        
        return int(grams) 
    return 0
            
    
    
print("Jambalaya")
text_parser(text1)


print("Hot Chocolate")
text_parser(text2)

print("Protein Powder")
text_parser(text3)

#uncomment when uncommenting picture taking
#cam.release()
#cam.destroyAllWindows()