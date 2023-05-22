from win32gui import FindWindow, GetWindowRect
import ctypes

def getscreensize(): #gets pixel width and height of current monitor
    user32 = ctypes.windll.user32
    h = user32.GetSystemMetrics(0)
    w = user32.GetSystemMetrics(1)
    return h, w

            
def getappsap(): #gets top-left pixel of Bluestacks, as well as window height and width
    window_handle = FindWindow(None, "Bluestacks")
    rect = GetWindowRect(window_handle)

    x = rect[0]
    y = rect[1] + 30
    w = rect[2] - x
    h = rect[3] - y

    return h, w, x, y
    
                    
            
