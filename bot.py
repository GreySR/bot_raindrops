import os
import cv2
import time
import win32api
import win32con
import numpy as np
from PIL import ImageGrab

# Функция делает скриншот заданной области(игрового поля)
def screenGrab():
	box = (9,55,456,534)
	im = ImageGrab.grab(box)
#	global string
	string = str(int(time.time()))
	im.save(string + '.png','PNG')
	circle(string)

# Функция ищет координаты кругов на скриншотах
# в которых находятся числа и знак	
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ДОБАВИТЬ ИСКЛЮЧЕНИЕ np.around attribute
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def circle(string):
	img = cv2.imread(string + '.png',0)
	number = cv2.imread(string + '.png',-1)
	img = cv2.medianBlur(img,5)
	cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

	circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=60,\
							param2=50,minRadius=0,maxRadius=0)
	print(circles)
	try:
		circles = np.uint16(np.around(circles))
	except AttributeError:
		pass
#	circles = np.uint16(np.around(circles.astype(np.double),3))
	if str(type(circles))=="<class 'NoneType'>":
		pass
	else:
		for i in circles[0,:]:
			cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
	#		cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3) # центр круга
			print(str(i[0]) + ' ' + str(i[1]))
			if i[1] > 40:
				pass
			else:
				num1 = number[(i[1]-17):i[1],(i[0]-12):(i[0]+21)] 
				cv2.imwrite(string + str(i) + '.png',num1)
	os.remove(string + '.png')
#		cv2.imshow('detected circles',num1)
#		cv2.waitKey(0)
#		cv2.destroyAllWindows()
#	cv2.imshow('detected circles',cimg)
#	cv2.waitKey(0)
#	cv2.destroyAllWindows()

# Функция распознает числа и знак в заданной области.
# Далее вызывает operation, получает результат и 
# передает клавиатуре.
def numberDetect(x,y): 
#
#   Распознование
#
	number = operation(5,7,'*')
#	keyboardInput(number)

# Функция принимает число и клавиатура вводит его 
def keyboardInput(number):
	for i in str(number):
		if i == '0':
			win32api.keybd_event(win32con.VK_NUMPAD0,0,0,0)
			win32api.keybd_event(win32con.VK_NUMPAD0,0,win32con.KEYEVENTF_KEYUP,0)
		elif i == '1':
			win32api.keybd_event(win32con.VK_NUMPAD1,0,0,0)
			win32api.keybd_event(win32con.VK_NUMPAD1,0,win32con.KEYEVENTF_KEYUP,0)
		elif i == '2':
			win32api.keybd_event(win32con.VK_NUMPAD2,0,0,0)
			win32api.keybd_event(win32con.VK_NUMPAD2,0,win32con.KEYEVENTF_KEYUP,0)	
		elif i == '3':
			win32api.keybd_event(win32con.VK_NUMPAD3,0,0,0)
			win32api.keybd_event(win32con.VK_NUMPAD3,0,win32con.KEYEVENTF_KEYUP,0)
		elif i == '4':
			win32api.keybd_event(win32con.VK_NUMPAD4,0,0,0)
			win32api.keybd_event(win32con.VK_NUMPAD4,0,win32con.KEYEVENTF_KEYUP,0)
		elif i == '5':
			win32api.keybd_event(win32con.VK_NUMPAD5,0,0,0)
			win32api.keybd_event(win32con.VK_NUMPAD5,0,win32con.KEYEVENTF_KEYUP,0)
		elif i == '6':
			win32api.keybd_event(win32con.VK_NUMPAD6,0,0,0)
			win32api.keybd_event(win32con.VK_NUMPAD6,0,win32con.KEYEVENTF_KEYUP,0)	
		elif i == '7':
			win32api.keybd_event(win32con.VK_NUMPAD7,0,0,0)
			win32api.keybd_event(win32con.VK_NUMPAD7,0,win32con.KEYEVENTF_KEYUP,0)
		elif i == '8':
			win32api.keybd_event(win32con.VK_NUMPAD8,0,0,0)
			win32api.keybd_event(win32con.VK_NUMPAD8,0,win32con.KEYEVENTF_KEYUP,0)
		elif i == '9':
			win32api.keybd_event(win32con.VK_NUMPAD9,0,0,0)
			win32api.keybd_event(win32con.VK_NUMPAD9,0,win32con.KEYEVENTF_KEYUP,0)	
	win32api.keybd_event(win32con.VK_RETURN,0,0,0)
	win32api.keybd_event(win32con.VK_RETURN,0,win32con.KEYEVENTF_KEYUP,0)	

# Функция принимает два числа и знак; выдает арифметический результат 	
def operation(a, b, strZnak):
	if strZnak == '+':
		return a + b
	elif strZnak == '-':
		return a - b
	elif strZnak == '*':
		return a * b
	else:
		return a // b
def main():
	while True:
		screenGrab()
#		print(operation(35,7,'/'))
if __name__ == '__main__':
	main()
	