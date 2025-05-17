import colorama as cr
from colorama import Fore as f
from colorama import Style as s
from textblob import TextBlob as tb
cr.init()
print(f"{f.CYAN}Welcome to Sentiment Spy! {s.RESET_ALL}")
un = str(input(f"{f.MAGENTA}Please Enter You Name : {s.RESET_ALL}")).strip()
if not un:
    un = "???"
ch = []
print(f"\n{f.CYAN}Hello, Agent {un}!")
print("Type a sentence and I will analyze your sentences with TextBlob and I will show you the sentiment.")
print(f"Type {f.YELLOW}'reset'{f.CYAN}, {f.YELLOW}'history'{f.CYAN}, or {f.YELLOW}'exit' {f.CYAN}to quit. {s.RESET_ALL}\n")
while True:
    ui = str(input(f"{f.GREEN}>> {s.RESET_ALL}")).strip()
    if not ui:
        print(f"{f.RED}Please enter some text or a valid command.{s.RESET_ALL}")
        continue
    if ui.lower() == "exit":
        print(f"\n{f.BLUE}🟧 Exiting Sentimal Spy. Farewell, Agent {un}!{s.RESET_ALL}\n")
        break
    elif ui.lower() == "reset":
        ch.clear()
        print(f"{f.CYAN}🎉 All conversation history cleared!{s.RESET_ALL}")
        continue
    elif ui.lower() == "history":
        if not ch:
            print(f"{f.YELLOW}No conversation history yet.{s.RESET_ALL}")
        else:
            print(f"{f.CYAN}📜 Conversation History :{s.RESET_ALL}")
            for i,(t,p,st) in enumerate(ch,start = 1):
                if st == "Positive":
                    clr = f.GREEN
                    emj = "😊"
                elif st == "Negative":
                    clr = f.RED
                    emj = "😢"
                else:
                    clr = f.YELLOW
                    emj = "😐"
                print(f"{i}. {clr}{emj} {t} (Polarity : {p:.2f}, {st}){s.RESET_ALL}")
        continue
    p = tb(ui).sentiment.polarity
    if p > .25:
        st = "Positive"
        clr = f.GREEN
        emj = "😊"
    elif p < -.25:
        st = "Negative"
        clr = f.RED
        emj = "😢"
    else:
        st = "Neutral"
        clr = f.YELLOW
        emj = "😐"
    ch.append((ui,p,st))
    print(f"{clr}{emj} {st} sentiment detected! (Polarity : {p:.2f}){s.RESET_ALL}")