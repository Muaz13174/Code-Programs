# for testing purposes only
from sys import exit as exit
from colorama import Fore as f
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