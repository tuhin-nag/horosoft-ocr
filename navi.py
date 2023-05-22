import pyautogui
import datetime
import time



    
def menu(startdt, appx, appy, apph, appw): #inputs all the datat received from user into main and moves to pp page
    pyautogui.click(appx + (0.5*appw),appy + (0.2*apph),1,1)

    #name
    pyautogui.write('xyz') 
    pyautogui.press('tab', 4)

    #city
    pyautogui.write('Mumbai')    
    pyautogui.press('tab', 2)

    #day
    pyautogui.press('enter')
    pyautogui.press('down', startdt.day - 1, 0.01)
    pyautogui.press('enter')

    pyautogui.press('tab')


    #month
    pyautogui.press('enter')
    pyautogui.press('down', startdt.month - 1, 0.01)
    pyautogui.press('enter')

    pyautogui.press('tab')

    #year
    today = datetime.date.today()
    nowyear = today.year

    yearCount = startdt.year - nowyear

    if yearCount < 0:
        pyautogui.press('enter')
        pyautogui.press('down', abs(yearCount), 0.01)
        pyautogui.press('enter')
    elif yearCount > 0:
        pyautogui.press('enter')
        pyautogui.press('up', abs(yearCount), 0.01)
        pyautogui.press('enter')

    pyautogui.press('tab')

    #hour
    pyautogui.press('enter')
    pyautogui.press('down', startdt.hour)
    pyautogui.press('enter')

    pyautogui.press('tab')

    #minute
    pyautogui.press('enter')
    pyautogui.press('down', startdt.minute, 0.01)
    pyautogui.press('enter')

    pyautogui.press('tab', 5)
    #submit , left menu
    pyautogui.press('enter',1,12)

    pyautogui.click(appx + (0.05*appw),appy + (0.05*apph),1,1)
    pyautogui.press('tab')
    pyautogui.press('down', 100)
    pyautogui.click(appx + (0.1*appw),appy + (0.1*apph),1,1)


def gotops(appx, appy, apph, appw): #goto prime significators
    pyautogui.click(appx + (0.05*appw),appy + (0.05*apph),1,1)
    
    pyautogui.moveTo(appx + (0.2*appw), appy + (0.36*apph))  
    time.sleep(1) 
    pyautogui.scroll(140)
    time.sleep(1) 

    
    pyautogui.click(appx + (0.2*appw),appy + (0.36*apph),1,1)

def gotopp(appx, appy, apph, appw): #goto planetary position
    pyautogui.click(appx + (0.05*appw),appy + (0.05*apph),1,1)
    pyautogui.moveTo(appx + (0.1*appw), appy + (0.5*apph)) 
    time.sleep(1) 
    pyautogui.scroll(-200)
    time.sleep(1) 
    pyautogui.scroll(-200)
    time.sleep(1) 


    pyautogui.click(appx + (0.1*appw),appy + (0.1*apph),1,1)

def getnextdt(startdt, currdt, enddt, interval, hpd, next): #give current dt and get next
    prevyear = currdt.year
    currdt = currdt + interval
    
    if currdt > enddt:
        next = False
    
    if currdt > (startdt + hpd):
        startdt = startdt + datetime.timedelta(days=1)
        currdt = startdt
        if startdt.weekday() == 5:
            startdt = startdt + datetime.timedelta(days=2)
            currdt = startdt
    return startdt, currdt, prevyear, next


def gotonextdt(prevyear, currdt, appx, appy, apph, appw): #navigate to given datetime
    pyautogui.click(appx + (0.9*appw),appy + (0.05*apph),1,1)
    pyautogui.press('down', 4, 0.01)
    pyautogui.press('enter')

    #day
    setfieldandgggonext(currdt.day - 1)

    #month    
    setfieldandgggonext(currdt.month - 1)
      
    #year
    if currdt.year > prevyear:
        pyautogui.press('enter')
        pyautogui.press('down', 1)
        pyautogui.press('enter')  
        prevyear += 1
    
    pyautogui.press('tab')

    #hour
    setfieldandgggonext(currdt.hour)

    #min
    setfieldandgggonext(currdt.minute)

    pyautogui.press('tab')
    pyautogui.press('enter')
    
    
def setfieldandgggonext(x):
    pyautogui.press('enter')
    pyautogui.press('up', 60, 0.001)
    pyautogui.press('down', x, 0.001)
    pyautogui.press('enter')

    pyautogui.press('tab')

