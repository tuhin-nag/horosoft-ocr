#TODO change hard coded column coordinates to variables with appsize

import layoutparser as lp
from PIL import ImageGrab
import matplotlib.pyplot as plt
import pyautogui
import pytesseract
import pandas as pd
import numpy as np
import cv2
from PIL import Image




def readdata(x, y, w, h):
    pyautogui.click(1500,120,1,1)
    #x = x y = y + 30 w = w - 150 h = h/1.9
    img1 = ImageGrab.grab(bbox=(x , y+30 , x + w , (y+h)/2.19))
    img = makebw(img1)
    

    ocr_agent = lp.ocr.TesseractAgent()
    res = ocr_agent.detect(img, return_response=True)

    #coords to filter columns from image
    y1, y2 = 150, 850
    plx1, plx2 = 0, 100  
    sgnx1, sgnx2 = 120, 240
    degreex1, degreex2 = 220, 400
    sgn2x1, sgn2x2 = 400, 500
    nakx1, nakx2 = 500, 600
    subx1, subx2 = 700, 800
    ssbx1, ssbx2 = 800, 900

    layout = ocr_agent.gather_data(res, agg_level=lp.TesseractFeatureType.WORD)
        # collect all the texts without coordinates

    pl = filterby(plx1, plx2, y1, y2, img, layout)
    sgn = filterby(sgnx1, sgnx2, y1, y2, img, layout)
    degree = filterby(degreex1, degreex2, y1, y2, img, layout)
    sgn2 = filterby(sgn2x1, sgn2x2, y1, y2, img, layout)
    nak = filterby(nakx1, nakx2, y1, y2, img, layout)
    sub = filterby(subx1, subx2, y1, y2, img, layout)
    ssb = filterby(ssbx1, ssbx2, y1, y2, img, layout)

  


    pllist = makelist(pl)
    sgnlist = makelist(sgn)
    degreelist = makelist(degree)
    sgn2list = makelist(sgn2)
    naklist = makelist(nak)
    sublist = makelist(sub)
    ssblist = makelist(ssb)

    degreelistfix = degreefix(degreelist)


    arr = [pllist, sgnlist, degreelistfix, sgn2list, naklist, sublist, ssblist]
    fixedarr = fixlen(arr)
    ls = transpose(fixedarr)
    return ls 

def makebw(img):
    width, height = img.size

        # Process every pixel
    for x in range(0,width):
        for y in range(0,height):
            cc = img.getpixel( (x,y) )
            if cc[0] > 100 or cc[1] > 100 or cc[2] > 100:
                nc = (255,255,255)
                img.putpixel( (x,y), nc)
               
    return img

def filterby(x1, x2, y1, y2, img, layout): #filters columns
    f = layout.filter_by(
        lp.Rectangle(x1, y1, x2, y2),soft_margin = {"left":10, "right":20}
    )
    out = lp.draw_text(img, f, font_size=16)
    return out

def cropimagehalfwidth(img): #reduces img width by half
    w, h = img.size
    cropped = img.crop((0, 0, w/2, h))
    return cropped

def converttolist(str): #converts ocr str output to list
    data = str.split('\n')
    data.pop(-1)

    for i in data:
        if i == '':
            data.remove(i)
    return data

def makelist(img): #makes list of values from image
    crop = cropimagehalfwidth(img)

    custom_config = r'--oem 3 --psm 6'
    str = pytesseract.image_to_string(crop, config=custom_config)
    data = converttolist(str)

    return data

def transpose(arr):
    ls = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
    return ls

def degreefix(ls):
    ls2 = []
    for item in ls:
        x = item.replace(" ", "")
        ls2.append(x)
    return ls2

def fixlen(arr):
    for i in range(len(arr)):
        while len(arr[i]) != 13:
            arr[i].append('0')

    return arr