# for testing purposes only
from sys import exit as exit
from colorama import Fore as f
import time as t
import threading as thr
def summation(start,end):
    d = 1
    if end < start:
        d = -1
    c = 0
    for i in range(start,end+1,d):
        c += i
    return c
#Summation Theorum:
#If a < b:
#-difference between summation from a to b and summation from -a to b is exactly equal to a
#a = 12
#b = 430
#print(summation(a,b) - summation(-a,b)) # = a
def sm():
    z = [["q","w","e","r","t","y","u","i","o","p"],["a","s","d","f","g","h","j","k","l"],["z","x","c","v","b","n","m"]]
    for i in z:
        for j in i:
            if j != z[-1][-1]:
                if j != z[0][-1] and j != z[1][-1]:
                    print(j+",",end = "")
                else:
                    print(j+",")
            else:
                print(j)
#how to check for existing files for cv2.imwrite()
def guf(bp):
    from pathlib import Path
    b = Path(bp)
    i = 1
    nwp = b
    while nwp.exists():
        nwp = b.with_name(f"{b.stem}_{i}{b.suffix}")
        i += 1
    return str(nwp)
def dsa(d):
    de = str(d)[-1]
    if de == "1":
        return f"{d}st"
    elif de == "2":
        return f"{d}nd"
    elif de == "3":
        return f"{d}rd"
    else:
        return f"{d}th"
def tsf(fn):
    from datetime import datetime as dt
    from pathlib import Path
    nwfn = Path(fn)
    return str(f"{nwfn.stem}_{dt.now().strftime(f"%A {dsa(dt.now().day)} %B %Y - %I:%M:%S %p")}{nwfn.suffix}")
import os
ip = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","Pictures","test pic.jpg")