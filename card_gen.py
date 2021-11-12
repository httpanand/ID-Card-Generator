__author__ = "Http Anand"

from PIL import Image, ImageDraw, ImageFont , ImageOps
import urllib.request

img_url = input('Enter icon URL :\n')
urllib.request.urlretrieve(img_url,"icon.png")

image = Image.new('RGB', (1000, 600), (255, 255, 255))
image = ImageOps.expand(image,border=10,fill='black')
draw = ImageDraw.Draw(image)

font = ImageFont.truetype(r'font\monalisa.ttf', 90)

heading = str('COMPANY')
draw.text((320, 120),heading,(0,0,0),font=font)

name = str(input('Enter name :\n'))
dob = str(input('Enter DOB (DD/MM/YY) :\n'))
age = str(input('Enter age :\n'))

font2 = ImageFont.truetype(r'font\monalisa.ttf', 50)
draw.text((350,300),'Name :',(0,0,0),font=font2)
draw.text((570,300),name,(0,0,0),font=font2)

draw.text((350,350),'DOB  :',(0,0,0),font=font2)
draw.text((570,350),dob,(0,0,0),font=font2)

draw.text((350,400),'AGE  :',(0,0,0),font=font2)
draw.text((570,400),age,(0,0,0),font=font2)

img = Image.open('icon.png')
img = img.resize((160, 160))
image.paste(img ,(150,295))


def save(): 
	image.save("output.png")

save()
