import gen
import input
import navi
import fetchdata


SCREEN_HEIGHT, SCREEN_WIDTH = gen.getscreensize()

APP_HEIGHT, APP_WIDTH, APP_X, APP_Y = gen.getappsap()

def main():
    startdt, enddt = input.getdtinput()
    interval = input.getinterval()
    hpd = input.hoursperday()

    navi.menu(startdt, APP_X, APP_Y, APP_HEIGHT, APP_WIDTH)
    currdt = startdt
    next = True

    fetchdata.fetchdata(next, APP_X, APP_Y, APP_HEIGHT, APP_WIDTH, startdt, currdt, enddt, interval, hpd)
    
    
    print('over')


if __name__ == '__main__':
    main()