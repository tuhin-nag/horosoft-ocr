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
    #x = x y = y + 30 w = w - 150 h = h/2.5
    img1 = ImageGrab.grab(bbox=(x , y+30 , x + w - 150 , (y+h)/2.5))
    img = makebw(img1)
    

    ocr_agent = lp.ocr.TesseractAgent()
    res = ocr_agent.detect(img, return_response=True)

    #coords to filter columns from image
    y1, y2 = 150, 840
    starx1, starx2 = 0, 100
    signi1x1, signi1x2 = 120, 300
    substarx1, substarx2 = 300, 500
    signi2x1, signi2x2 = 500, 800

    layout = ocr_agent.gather_data(res, agg_level=lp.TesseractFeatureType.WORD)
        # collect all the texts without coordinates

    star = filterby(starx1, starx2, y1, y2, img, layout)

    signi1 = filterby(signi1x1, signi1x2, y1, y2, img, layout)

    substar = filterby(substarx1, substarx2, y1, y2, img, layout)

    signi2 = filterby(signi2x1, signi2x2, y1, y2, img, layout)



    starlist = makelist(star)
    signi1list = makelist(signi1)
    substarlist = makelist(substar)
    signi2list = makelist(signi2)

    signi1listfix = fixlength(fixcommas(signi1list))
    signi2listfix = fixlength(fixcommas(signi2list))


    arr = [starlist, signi1listfix, substarlist, signi2listfix]
    ls = transpose(arr)
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

def fixcommas(data):

    fixed = []
    for item in data:
        newitem = ''
        for i in range(0, len(item)):
            try: 
                if i == len(item) - 1:
                    newitem += item[i]
                    continue
                if len(item) == 1:
                    newitem += item[i] + ','
                if int(item[i]) == 1 and item[i + 2] == ',':
                    newitem += item[i]
                elif int(item[i]) == 1 and i == 0 and int(item[i + 2]) != 0:
                    newitem += item[i] + ','
                elif int(item[i]) == 1 and item[i + 1] == ',':
                    newitem += item[i] + ','
                elif int(item[i]) == 1 and (int(item[i + 1]) != 0 or 1 or 2):
                    newitem += item[i]
                elif int(item[i]) == 1 and int(item[i + 2]) != 0:
                    newitem += item[i] + ','
                elif int(item[i]) == 1:
                    newitem += item[i]
                if int(item[i]) > 1:
                    newitem += item[i] + ','
                if int(item[i]) < 1:
                    newitem += item[i] + ','
            except IndexError:
                newitem += item[i]
                    
            except:
                continue
        if newitem[-1] == ',':
            newitem = newitem.rstrip(newitem[-1])    
                
        
        fixed.append(newitem)       
                    
    return fixed

# To make table appear in same format as app
def transpose(arr):
    ls = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
    return ls


# In case OCR doesnt read all numbers, and the list has less than 9 items TODO - error log
def fixlength(data):
    while len(data) != 9:
        data.append('0')
    return data