import cv2
import pytesseract
import PIL.Image

cam = cv2.VideoCapture(0)

cv2.namedWindow("Python Webcam")

img_counter = 0
my_config = r"--psm 3 --oem 3"

while True:
    ret, frame = cam.read()
    if not ret:
        print('failed to grab frame')
        break
    cv2.imshow('test', frame)
    k = cv2.waitKey(1)

    if k % 256 == 27:
        print("Escape hit")
        break
    elif k % 256 == 32:
        img_name = f"opencv_frame_{img_counter}.png"
        cv2.imwrite(img_name, frame)
        print('screenshot')
        text = pytesseract.image_to_string(PIL.Image.open(f"opencv_frame_{img_counter}.png"), config=my_config)
        print(text)
        img_counter += 1





cam.release()
#cam.destroyAllWindows()