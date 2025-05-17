from random import choice as ch
from colorama import init as i
from colorama import Fore as f
from colorama import Style as s
from time import sleep as slp
from pygame.mixer import music as music
from pygame.mixer import init as it
i(autoreset = True)
def pms():
    it()
    music.load("Ding.mp3")
    music.play()
    print(f"{f.GREEN}Done!{s.RESET_ALL}")
    while music.get_busy():
        continue
def dr():
    it()
    music.load("Drum Roll.mp3")
    music.play()
    while music.get_busy():
        continue
def win(p,a):
    ww = ""
    if (p == "R" and a == "S") or (p == "P" and a == "R") or (p == "S" and a == "P"):
        ww = "Player"
    elif (p == "R" and a == "P") or (p == "P" and a == "S") or (p == "S" and a == "R"):
        ww = "AI"
    else:
        ww = "Tie"
    return ww
def pc():
    c = str(input(f"{f.YELLOW}What do you pick? (rock/paper/scissors) :{s.RESET_ALL} ")).lower()
    if c == "rock":
        return "R"
    elif c == "paper":
        return "P"
    elif c == "scissors":
        return "S"
    else:
        print(f"{f.RED}I don't understand you choice.{s.RESET_ALL}")
        pc()
def ac():
    return ch(["R","P","S"])
def rps():
    pp = 0
    ap = 0
    print(f"{f.LIGHTCYAN_EX}Welcome to Rock-Paper-Scissors!{s.RESET_ALL}")
    pn = str(input(f"{f.GREEN}What is you name? :{s.RESET_ALL} "))
    while True:
        pw = pc()
        print(f"{f.LIGHTBLACK_EX}Computer Choosing.....{s.RESET_ALL}")
        aw = ac()
        slp(1)
        pms()
        e = win(pw,aw)
        emj = ["🥌","📰","✂️"]
        pe = ""
        ae = ""
        if pw == "R":
            pe = emj[0]
        elif pw == "P":
            pe = emj[1]
        elif pw == "S":
            pe = emj[2]
        if aw == "R":
            ae = emj[0]
        elif aw == "P":
            ae = emj[1]
        elif aw == "S":
            ae = emj[2]
        dr()
        d = ""
        if e == "Player":
            d = ">"
        elif e == "AI":
            d = "<"
        else:
            d = "="
        print(pe+" "+d+" "+ae)
        slp(1)
        if e == "Player":
            print(f"{f.GREEN}Congratulations! {pn}, you have won the game!{s.RESET_ALL}")
            pp += 1
            it()
            music.load("Win.mp3")
            music.play()
            while music.get_busy():
                continue
        elif e == "AI":
            ap += 1
            print(f"{f.RED}Aww, too bad!{s.RESET_ALL}")
            it()
            music.load("Lose.mp3")
            music.play()
            while music.get_busy():
                continue
        else:
            print(f"{f.BLUE}It's a draw!")
            it()
            music.load("Tie.mp3")
            music.play()
            while music.get_busy():
                continue
        print(f"{f.CYAN}Score {f.GREEN}{pp}{f.CYAN}:{f.RED}{ap}{s.RESET_ALL}")
        pa = str(input("\nDo you want to play again? (yes/no) : ")).lower()
        if pa != "yes":
            print("Thank you for playing!")
            break
if __name__ == "__main__":
    rps()