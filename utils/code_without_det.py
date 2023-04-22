from PIL import Image, ImageDraw, ImageFont, ImageOps
import pandas as pd
import cv2

form = pd.read_excel("Database.xlsx")
name_list = form['Name'].to_list()
email_list=form['Email'].to_list()
id_list=form['id'].to_list()
uni_list=form['university'].to_list()

total = len(name_list)
ei=0
while (ei<total):
	i=name_list[ei]
	uni_name=uni_list[ei]
	photolocation="images/"+id_list[ei]


	filenamess=name_list[ei].strip()+" - "+email_list[ei].strip()+".png"

	font = ImageFont.truetype("./UN Bangla Font/UNBangla-Bold.ttf", 48)
	font2 = ImageFont.truetype("./UN Bangla Font/UNBangla-Regular.ttf", 28)



	im = Image.open("frame 6th x.png")
	person=Image.open(photolocation)

	MAX_H,MAX_W = 1042,1042
	current_h, pad = 790, 5


	d = ImageDraw.Draw(im)
	w, h = d.textsize(i, font=font)
	location = ((MAX_W - w) / 2, current_h)
	text_color = (256,256,256)
	d.text(location, i, fill=text_color,font=font)


	MAX_H2,MAX_W2 = 1042,1042
	current_h2, pad2 = 855, 5

	d2 = ImageDraw.Draw(im)
	w2, h2 = d2.textsize(uni_name, font=font2)
	location2 = ((MAX_W2 - w2) / 2, current_h2)
	text_color = (256,256,256)
	d2.text(location2, uni_name, fill=text_color,font=font2)




	person = person.resize((310,310), Image.ANTIALIAS)
	
	bigsize = (person.size[0], person.size[1])
	mask = Image.new('L', bigsize, 0)
	draw = ImageDraw.Draw(mask) 
	draw.ellipse((0, 0) + bigsize, fill=255)
	mask = mask.resize(person.size, Image.ANTIALIAS)
	person.putalpha(mask)
	

	#im.paste(person, (375, 330))
	im=im.resize(im.size,Image.ANTIALIAS)
	

	saveimg = Image.new('RGB', im.size, color = 'white')
	saveimg.paste(im,(0,0))
	saveimg.paste(person, (370, 325),person)

	saveimg.save("files/"+filenamess)
	print(ei+1,"--", i, "----- Done---  ",filenamess)
	ei=ei+1