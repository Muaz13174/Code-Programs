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
    #return str(f"{nwfn.stem}_{dt.now().strftime(f"%A {dsa(dt.now().day)} %B %Y - %I:%M:%S %p")}{nwfn.suffix}")
import os
ip = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","Pictures","test pic.jpg")
def factors_of_a_number(num):
    fac = [1]
    from math import floor as floor
    for i in range(2,num,1):
        if num%i == 0:
            fac.append(i)
        else:
            pass
    fac.append(num)
    return fac
def pair_fac(num):
    fac = factors_of_a_number(num)
    li = 0
    ri = -1
    pair_facs_list = []
    while len(fac) > 2:
        pair_facs_list.append([fac[li],fac[ri]])
        fac = fac[1:-1]
    if len(fac) == 2:
        pair_facs_list.append(fac)
    elif len(fac) == 1:
        pair_facs_list.append(fac[0],fac[0])
    return pair_facs_list
def facrun():
    while True:
        try:
            num = int(input("Enter number : "))
            fac = factors_of_a_number(num)
            if len(fac) == 1:
                print(f"The factor of {num} is {fac[0]}.")
            elif len(fac) == 2:
                print(f"The factors of {num} are {fac[0]} and {fac[1]}.")
            elif len(fac) >= 3:
                print(f"The factors of {num} are",", ".join(map(str,fac[0:-1])),"and",str(fac[-1]) + ".")
        except ValueError as e:
            print(f"Error : {e}")
            break
def color_generator():
    from random import randint as r
    return [r(0,255),r(0,255),r(0,255)]