import re
import random as r
from colorama import Fore as f
from colorama import init as i
i(autoreset = True)
d = {
    "beaches":["Bali","Maldives","Phuket"],
    "mountains":["Swiss Alps","Rocky Mountains","Himalayas"],
    "cities":["Tokyo","Paris","New York"]
}
j = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]
def sh():
    print(f"{f.MAGENTA}\nI can:")
    print(f"{f.GREEN}- Suggest travel spots (say 'recommendation')\n- Offer packing tips (say 'packing')\n- Tell a joke (say 'joke')")
    print(f"{f.CYAN}Type 'exit' or 'bye' to end.\n")
def ni(t):
    return re.sub(r"\s+"," ",t.strip().lower())
def rec():
    print(f"{f.CYAN}TravelBot : beaches, mountains or cities?")
    p = str(input(f"{f.YELLOW}You : "))
    p = ni(p)
    if p in d:
        s = r.choice(d[p])
        print(f"{f.GREEN}How about {s}?")
        print(f"{f.CYAN}TravelBot : Do you like it? (yes/no)")
        a = str(input(f"{f.YELLOW}You : ")).lower()
        if a == "yes":
            print(f"{f.GREEN}TravelBot : Awesome! Enjoy {s}!")
        elif a == "no":
            print(f"{f.RED}TravelBot : Let's try another.")
            rec()
        else:
            print(f"{f.RED}TravelBot : I'll suggest again.")
            rec()
    else:
        print(f"{f.RED}TravelBot : Sorry, I don't have that type of destination")
    sh()
def pt():
    print(f"{f.CYAN}TravelBot : Where to?")
    l = ni(str(input(f"{f.YELLOW}You : ")))
    print(f"{f.CYAN}TravelBot : How many days?")
    day = int(input(f"{f.YELLOW}You : "))
    print(f"{f.GREEN}TravelBot : Packing tips for {day} days in {l}:\n- Pack versatile clothes.\n- Bring chargers/adapters.\n- Check the weather forecast.")
def tj():
    print(f"{f.YELLOW}TravelBot : {r.choice(j)}")
def c():
    print(f"{f.CYAN}Hello! I'm TravelBot.")
    n = str(input(f"{f.YELLOW}Your name? : "))
    print(f"{f.GREEN}Nice to meet you, {n}!")
    sh()
    while True:
        ui = ni(str(input(f"{f.YELLOW}{n} : ")))
        if "recommend" in ui or "suggest" in ui:
            rec()
        elif "pack" in ui or "packing" in ui:
            pt()
        elif "joke" in ui or "funny" in ui:
            tj()
        elif "help" in ui:
            sh()
        elif "exit" in ui or "bye" in ui:
            print(f"{f.CYAN}TravelBot : Safe travels! Goodbye!")
            break
        else:
            print(f"{f.RED}TravelBot : Could you rephrase?")
if __name__ == "__main__":
    c()