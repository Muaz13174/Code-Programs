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
#summation(a,b) - summation(-a,b) = a
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
    date_time = dt.now().strftime(f"%A {dsa(dt.now().day)} %B %Y - %I:%M:%S %p")
    return str(f"{nwfn.stem}_{date_time}{nwfn.suffix}")
import os
ip = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","Pictures","test pic.jpg")
def factors_of_a_number(num : int):
    if not isinstance(num,int):
        raise TypeError(f"Expected int, got {type(num).__name__} instead.")
    fac = [1]
    for i in range(2,num,1):
        if num%i == 0:
            fac.append(i)
        else:
            pass
    fac.append(num)
    return fac
def pair_fac(num : int):
    if not isinstance(num,int):
        raise TypeError(f"Expected int, got {type(num).__name__} instead.")
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
        pair_facs_list.append([fac[0],fac[0]])
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
    return (r(0,255),r(0,255),r(0,255))
def is_prime(num : int):
    if not isinstance(num,int):
        raise TypeError(f"Expected int, got {type(num).__name__} instead.")
    divisibles = []
    for i in range(1,num+2):
        if num%i == 0:
            divisibles.append(i)
    if len(divisibles) == 2:
        return True
    else:
        return False
def prime_fac(num : int):
    if not isinstance(num,int):
        raise TypeError(f"Expected int, got {type(num).__name__} instead.")
    prime = 2
    prime_factors = []
    store = num
    prime_loop = True
    while True:
        prime_loop = True
        if store == 1:
            break
        if store%prime == 0:
            prime_factors.append(prime)
            store = store/prime
            continue
        else:
            prime += 1
            if is_prime(prime):
                continue
            else:
                while prime_loop:
                    prime += 1
                    if is_prime(prime):
                        prime_loop = False
    return prime_factors
def ask_for_prime_fac():
    try:
        num = int(input("Enter a whole number to prime factorise : "))
    except ValueError as ve:
        print("Error : {ve}")
        return
    str_of_sequence = [str(p) for p in prime_fac(num)]
    print(f"The prime factor(s) of {num} are {' × '.join(str_of_sequence)} | {num} = {' × '.join(str_of_sequence)}")
def country_order_randomizer():
    from random import shuffle as shuffle
    from random import randint as randint
    countries = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon","Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo","Costa Rica","Croatia","Cuba","Cyprus","Czech Republic","Democratic Republic of the Congo","Denmark","Djibouti","Dominica","Dominican Republic","East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Ivory Coast","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","North Korea","South Korea","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Macedonia","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]
    times = randint(10,200)
    randlist = countries
    for i in range(times+1):
        shuffle(randlist)
    the_str = ""
    for c in randlist:
        if c == randlist(len(randlist)-1):
            the_str += str(c)
            break
        else:
            the_str += str(c)+","
    return [randlist,the_str,times]
def nth_prime(nth:int):
    if not isinstance(nth,int):
        raise TypeError(f"Expected int, got {type(nth).__name__} instead.")
    primes_list = []
    prime = 0
    while True:
        if is_prime(prime):
            primes_list.append(prime)
        if len(primes_list) == nth:
            return primes_list[-1]
        prime += 1
def show_nth_prime():
    try:
        num = int(input("Enter the term number of primes : "))
    except ValueError as e:
        raise TypeError(f"Expected int, got {type(num).__name__} instead.")
    prime = show_nth_prime(num)
    term = dsa(num)
    print(f"The {term} prime is {prime}.")
    return
from typing import Union as U
from decimal import Decimal
from fractions import Fraction
from numbers import Real
def add_all(*args:U[int,float,Decimal,Fraction]):
    the_sum = 0
    for i in args:
        if not (isinstance(i,Real) and type(i) is not bool):
            raise TypeError(f"Expected Real, got {type(i).__name__} instead.")
        the_sum += i
    return the_sum
def multiply_all(*args:U[int,float,Decimal,Fraction]):
    the_product = 0
    for i in args:
        if not (isinstance(i,Real) and type(i) is not bool):
            raise TypeError(f"Expected Real, got {type(i).__name__} instead.")
        the_product = i * the_product
    return the_product