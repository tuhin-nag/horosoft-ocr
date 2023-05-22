import os
import time

def pptolist(arr, dt):
    
    try:
        os.mkdir("./planet/" + dt.strftime("%Y"))
    except:
        time.sleep(0.0001)

    try:
        os.mkdir("./planet/" + dt.strftime("%Y") + "/" + dt.strftime("%m"))
    except:
        time.sleep(0.0001)

    if not os.path.isfile("./planet/" + dt.strftime("%Y") + "/" + dt.strftime("%m") + "/" + dt.strftime("%d%m%y") + "-planet.txt"): 
        f= open("./planet/" + dt.strftime("%Y") + "/" +  dt.strftime("%m") + "/" +  dt.strftime("%d%m%y") + "-planet.txt","a+")
        f.write("Date Time Planet ZOD Degree SGN NAK SUB SSB NaN\n")
        f.close()

    f= open("./planet/" + dt.strftime("%Y") + "/" +  dt.strftime("%m") + "/" +  dt.strftime("%d%m%y") + "-planet.txt","a+")
    f.close()
    with open("./planet/" + dt.strftime("%Y") + "/" +  dt.strftime("%m") + "/" +  dt.strftime("%d%m%y") + "-planet.txt","a+") as f:       
        writelist(arr, f, dt)

    

def pstolist(arr, dt):
    
    try:
        os.mkdir("./prime/" + dt.strftime("%Y"))
    except:
        time.sleep(0.0001)

    try:
        os.mkdir("./prime/" + dt.strftime("%Y") + "/" + dt.strftime("%m"))
    except:
        time.sleep(0.0001)

    if not os.path.isfile("./prime/" + dt.strftime("%Y") + "/" + dt.strftime("%m") + "/" + dt.strftime("%d%m%y") + "-prime.txt"): 
        f= open("./prime/" + dt.strftime("%Y") + "/" +  dt.strftime("%m") + "/" +  dt.strftime("%d%m%y") + "-prime.txt","a+")
        f.write("Date Time Star Signi SubStar Signi NaN\n")
        f.close()

    f= open("./prime/" + dt.strftime("%Y") + "/" +  dt.strftime("%m") + "/" +  dt.strftime("%d%m%y") + "-prime.txt","a+")
    f.close()
    with open("./prime/" + dt.strftime("%Y") + "/" +  dt.strftime("%m") + "/" +  dt.strftime("%d%m%y") + "-prime.txt","a+") as f:
       writelist(arr, f, dt)

    f.close()



def writelist(arr, f, dt):
    rows = len(arr)
    cols = len(arr[0])
    for i in range(rows):
        f.write(dt.strftime("%d/%m/%y %H:%M "))
        for j in range(cols):
            f.write("%s " % arr[i][j])
        f.write("\n")    


