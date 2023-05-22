import navi
import time
import readps
import readpp
import tolist
import datetime

def fetchdata(next, x, y, h, w, startdt, currdt, enddt, interval, hpd):
    while next:
        time.sleep(0.5)
        pparr = readpp.readdata(x, y, w, h)
        time.sleep(0.5)
        tolist.pptolist(pparr, currdt)
        time.sleep(0.5)

        navi.gotops(x, y, h, w)
        time.sleep(0.5)

        #OCR PS
        psarr = readps.readdata(x, y, w, h)
        time.sleep(0.5)
        tolist.pstolist(psarr, currdt)
        time.sleep(0.5)

        navi.gotopp(x, y, h, w)
        time.sleep(0.5)

        startdt, currdt, prevyear, next = navi.getnextdt(startdt, currdt, enddt, interval, hpd, next)

        navi.gotonextdt(prevyear, currdt, x, y, h, w)
        time.sleep(1)