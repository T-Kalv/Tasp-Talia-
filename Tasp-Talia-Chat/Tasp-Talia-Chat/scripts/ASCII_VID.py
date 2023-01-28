#Plays a vid into the terminal using ASCII
import os 
import sys
import cv2
from PIL import Image
from playsound import playsound
import pyttsx3
ASCII_Characters = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
engine = pyttsx3.init()
engine.setProperty('rate', 220) 
engine.say("Enter File Path")
engine.runAndWait()
response = input("Enter File Path: ")
cap = cv2.VideoCapture(response)

def resize_image(image ,new_width=70):
	width,height = image.size
	aspect_ratio = height/width
	new_height = int(aspect_ratio * new_width)
	resized_image = image.resize((new_width,new_height)).convert('L')
	return resized_image

def pixel_to_characters(image):
	pixels = image.getdata()
	char = "".join([ASCII_Characters[pixel//25] for pixel in pixels])
	return char

def create_new_frame(image,new_width=70):
	new_image_data = pixel_to_characters(resize_image(image))
	sum_of_pixels = len(new_image_data)
	ASCII_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, sum_of_pixels, new_width)])
	sys.stdout.write(ASCII_image)
	os.system('cls' if os.name == 'nt' else 'clear')


os.system(response)
while (True):	
	ret,frame = cap.read()
	#cv2.imshow("Video Source",frame)
	create_new_frame(Image.fromarray(frame))
	#cv2.waitKey(1)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
engine.say("Hi, How Can I Help?")
print("Hi, How Can I Help? 💬")
engine.runAndWait()