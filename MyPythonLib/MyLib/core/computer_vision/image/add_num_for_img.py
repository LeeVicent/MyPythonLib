#_*_ coding: utf-8 _*_
__author__ = "Net"

from PIL import Image,ImageDraw,ImageFont

import random
msgNum = str(random.randint(1, 99))

#Read image
img = Image.open('D:\\壁纸.jpg')
width, height = img.size   #size为元组， e.g.  (1920, 1080)
wDraw = 0.8 * width
hDraw = 0.08 * width

# Draw image
font = ImageFont.truetype('D:\\Lanehum.ttf', 30)  # use absolute font path to fix 'IOError: cannot open resource'
draw = ImageDraw.Draw(img)
draw.text((wDraw,hDraw), msgNum, font = font, fill = (255, 33, 33))

# Save image
img.save('add_num.png', 'png')
