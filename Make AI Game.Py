import random as r
from colorama import init as i
from colorama import Fore as f
from colorama import Style as s
i(autoreset = True)
def db(b):
    print()
    def c(cell):
        cl = str(cell)
        if cl == "X":
            return f.RED + cl + s.RESET_ALL
        elif cl == "O":
            return f.BLUE + cl + s.RESET_ALL
        else:
            return f.YELLOW + cl + s.RESET_ALL
    print(f" {c(b[0])}|{c(b[1])}|{c(b[2])}")
    print(f"{f.CYAN}-------{s.RESET_ALL}")
    print(f" {c(b[3])}|{c(b[4])}|{c(b[5])}")
    print(f"{f.CYAN}-------{s.RESET_ALL}")
    print(f" {c(b[6])}|{c(b[7])}|{c(b[8])}")
    print()
def pc():
    sb = ""
    while sb not in ["X","O"]:
        sb = str(input(f"{f.GREEN}Do you want to be X or O? :{s.RESET_ALL} ")).upper()
    if sb == "X":
        return ("X","O")
    elif sb == "O":
        return ("O","X")
def pm(b,sb):
    m = -1
    while m not in range(1,10) or not b[m - 1].isdigit():
        try:
            m = int(input("Enter your move (1-9) : "))
            if m not in range(1,10) or not b[m - 1].isdigit():
                print("Invalid move. Please try again.")
        except ValueError:
            print("Please enter a number between 1 and 9")
    b[m - 1] = sb
def cw(b,sb):
    wc = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for c in wc:
        if b[c[0]] == b[c[1]] == b[c[2]] == sb:
            return True
    return False
def am(b,asb,psb):
    for i in range(9):
        if b[i].isdigit():
            bc = b.copy()
            bc[i] = asb
            if cw(bc,asb):
                b[i] = asb
                return
    for i in range(9):
        if b[i].isdigit():
            bc = b.copy()
            bc[i] = psb
            if cw(bc,psb):
                b[i] = asb
                return
    psm = [i for i in range(9) if b[i].isdigit()]
    m = r.choice(psm)
    b[m] = asb
def cf(b):
    return all(not spot.isdigit() for spot in b)
def ttt():
    print("Welcome to Tic-Tac-Toe!")
    pn = str(input(f"{f.GREEN}What is you name? :{s.RESET_ALL} "))
    while True:
        b = ["1","2","3","4","5","6","7","8","9"]
        psb,asb = pc()
        t = "Player"
        go = True
        while go:
            db(b)
            if t == "Player":
                pm(b,psb)
                if cw(b,psb):
                    db(b)
                    print(f"Congratulations! {pn}, you have won the game!")
                    go = False
                else:
                    if cf(b):
                        db(b)
                        print("It's a tie!")
                        break
                    else:
                        t = "AI"
            else:
                am(b,asb,psb)
                if cw(b,asb):
                    db(b)
                    print("AI has won the game!")
                    go = False
                else:
                    if cf(b):
                        db(b)
                        print("It's a tie!")
                        break
                    else:
                        t = "Player"
        pa = str(input("Do you want to play again? (yes/no) : ")).lower()
        if pa != "yes":
            print("Thank you for playing!")
            break
if __name__ == "__main__":
    ttt()