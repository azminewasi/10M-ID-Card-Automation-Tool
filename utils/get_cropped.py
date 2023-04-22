from PIL import Image, ImageDraw, ImageFont, ImageOps
import pandas as pd
import cv2
import time


def detect(gray, frame):
	faces=face_cascade.detectMultiScale(gray,1.5,5)
	for (x,y,w,h) in faces:
		data=[x,y,w,h]
		return data

def face_location_processing (h,w,data,img,name):

	
	f_x=data[0]+data[2]/4
	f_y=data[1]+data[3]/4
	f_h=data[3]
	f_w=data[2]



	if f_h>f_w:
		f_h=f_h+(h*0.5)
		if f_h>h:
			f_h=h
	f_w=f_h

	if f_w>f_h:
		f_w=f_w+(w*0.5)
		if f_w>w:
			f_w=w
	f_h=f_w

	

	crop_img = img[int(f_y-(f_h/2)):int(f_y+f_h), int(f_x-(f_w/2)):int(f_x+f_w)]
	cv2.imwrite("auto_cropped/"+name, crop_img)
	return crop_img


def get_cropped():
    face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
    failed=[]
    
    face_location_processing (i_height, i_width,canvas_data,imgData,id_list[ei]+".png")