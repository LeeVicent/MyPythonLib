#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

from PIL import Image

import cv2
import time
import os
import numpy as np
import ToolBox.ImageProcessTool as  IPT
import sys

sys.path.append("F:\文档\Visual Studio 2015\Projects\MyPytho nLib\MyPythonLib\MyLib")

def join_image(image1, image2):
    UNIT_SIZE = 40#高
    TARGET_WIDTH = 28 * 2 # 拼接完后的横向长度

    path = "./Numbers/"
    images = [] # 先存储所有的图像的名称
    images.append(image1)
    images.append(image2)

    im = Image.open(path + image1) 

    imagefile = []  #此列表存储图像对象
    j = 0
        #for j in range(2):
        #    imagefile.append(Image.open("1.png")
        #    imagefile[j].show()
        
    target = Image.new('RGB', (TARGET_WIDTH, UNIT_SIZE))    #创建空目标图像
    left = 0
    right = UNIT_SIZE
    for image in imagefile:     
        target.paste(image, (left, 0, right, UNIT_SIZE))# 将image复制到target的指定位置中
        left += UNIT_SIZE # left是左上角的横坐标，依次递增
        right += UNIT_SIZE # right是右下的横坐标，依次递增
        quality_value = 100 # quality来指定生成图片的质量，范围是0～100
        target.save(path+'/result/'+os.path.splitext(images[i*2+j])[0]+'.png', quality = quality_value)
    imagefile = []


def ImageProcess():
    while True:
        Number = raw_input("please input num:")
        SrcImgPath = './Numbers/OCR.png'
        SrcImg = cv2.imread(SrcImgPath)
        GrayImg = cv2.cvtColor(SrcImg, cv2.COLOR_BGR2GRAY)

        TemplatePath = './Numbers/' + Number + '.png'
        TemplateImg = cv2.imread(TemplatePath, 0)
        Height, Weight = TemplateImg.shape
        MatchResult = cv2.matchTemplate(image=GrayImg, templ=TemplateImg, method=cv2.TM_CCOEFF_NORMED)

        DrawImg = SrcImg.copy()
        Thresh = 0.8
        Loc = np.where(MatchResult >= Thresh)

        for pt in zip(*Loc[:: -1]):  
            Roi_xywh = [pt[0], pt[1], Weight, Height]
            IPT.drawRoi(img=DrawImg, roi=Roi_xywh, roiType=IPT.ROI_TYPE_XYWH, color=(255, 0, 0))
        cv2.imshow('MatchResult', MatchResult)
        cv2.imshow('Result', DrawImg)
        cv2.namedWindow('Result')
        cv2.namedWindow('MatchResult')

        Key = chr(cv2.waitKey() & 255)
        if Key == 'q':
            pass
        elif '0' <= Key <= '9':
            print 'Key: ', Key
            Number = Key
          
if __name__ == '__main__':
    ImageProcess()
    #join_image("1.png", "2.png")
