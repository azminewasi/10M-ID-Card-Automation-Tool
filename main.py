# Importing Necessary Modules
# Install them if you don't have them. 

from PIL import Image, ImageDraw, ImageFont, ImageOps #Image Processing
import pandas as pd # Data Management
import cv2 # Face Detection
from utils.BG_REMOVAL import bg_remover #BG Removal
from utils.fd import face_location_processing, detect


# List of failed tasks
failed=[]

# Data Loading
form = pd.read_excel("Database.xlsx")
name_list = form['Name'].to_list()
id_list=form['id'].to_list()
designation_list=form['Designation'].to_list()
total = len(name_list)
ei=0


while (ei<total): # Loop through database
	i=name_list[ei]
	uni_name=designation_list[ei]
	photolocation=r"./images/"+id_list[ei]   # Image loading
 
	print("Currently loading... :",id_list[ei])
	filename_for_saving=name_list[ei].strip()+" - "+designation_list[ei].strip()+".png"

# fonts
	font = ImageFont.truetype("./font/Poppins-Medium.ttf", 38)  
	font2 = ImageFont.truetype("./font/Poppins-Regular.ttf", 24)

# Base image loading...
	im = Image.open("0BaseFrame.png")
	imgData=cv2.imread(r"./images/"+id_list[ei])

# Error Checking - Image Loading
	if type(imgData)==type(None):
		print("Image loading Failed")
		ei=ei+1
		failed.append(str(id_list[ei])+"  -  Image loading Failed")
		continue

	i_height, i_width, i_channels = imgData.shape
	print("Image Size: "+str(i_height)+"x"+str(i_width))

# Face Detection
	gray=cv2.cvtColor(imgData, cv2.COLOR_BGR2GRAY)
	canvas_data=detect(gray,imgData)
 
# Error Checking - Face Detection
	if canvas_data==None:
		print("Face detection Failed")
		ei=ei+1
		failed.append(str(id_list[ei])+"  -  Face detection Failed")
		continue

# Face Location Processing
	person=face_location_processing (i_height, i_width,canvas_data,imgData,id_list[ei]+".png")
 
# Name Placement
	MAX_H,MAX_W = 1004,651
	current_h, pad = 220, 5
	d = ImageDraw.Draw(im)
	w, h = d.textsize(i, font=font)
	location = ((MAX_W - w) / 2, current_h)
	text_color = (0,0,0)
	d.text(location, i, fill=text_color,font=font)

# Designation Placement
	MAX_H2,MAX_W2 = 1004,651
	current_h2, pad2 = 270, 5
	d2 = ImageDraw.Draw(im)
	w2, h2 = d2.textsize(uni_name, font=font2)
	location2 = ((MAX_W2 - w2) / 2, current_h2)
	text_color = (0,0,0)
	d2.text(location2, uni_name, fill=text_color,font=font2)


# BG Removal
	color_coverted = cv2.cvtColor(person, cv2.COLOR_BGR2RGB)
	person = Image.fromarray(color_coverted)

	person = person.resize((651,651), Image.ANTIALIAS)
	person_nBG = bg_remover(person)
	
	im=im.resize(im.size,Image.ANTIALIAS)

# Pasting All layers in one frame
	saveimg = Image.new('RGB', im.size, color = 'white')
	saveimg.paste(im,(0,0))
	saveimg.paste(person_nBG, (0,353),person_nBG)

# File saving as png
	saveimg.save("files/"+filename_for_saving)
	print(ei+1,"--", i, "----- Done---  ",filename_for_saving)
# File saving as pdf
	pdfimg=saveimg.convert('RGB')
	pdfimg.save("pdf_files/"+filename_for_saving.replace("png","pdf"))
	ei=ei+1
 
# Errors list
for file in failed:
	print(file)