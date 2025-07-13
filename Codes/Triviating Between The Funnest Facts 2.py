import requests as rqs
import random as rd
import html
import time as t
import threading as thr
import winsound as ws
time_up = False
def countdown(seconds):
    global time_up
    bar_length = 20
    for i in range(seconds):
        if time_up:
            return
        r = seconds - i
        f = int(bar_length * (r/seconds))
        b = "#" * f + "-" * (bar_length - f)
        print(f"\r⏳ Time left: [{b}] {r}s", end = "",flush = True)
        t.sleep(1)
    if not time_up:
        time_up = True
        print("\r⏰ Time's up!")
        ws.Beep(1000,500)
EDUCATION_CATEGORY_ID = rd.randint(9,32)
NUM_OF_QUESTIONS = 0
while 5 <= NUM_OF_QUESTIONS <= 50:
    try:
        NUM_OF_QUESTIONS = int(input("Enter a number between 1 to 46 : ")) + 4
    except ValueError:
        print("\nInvalid! Enter a number.")
    print("\nYou can only pick numbers between 1 and 46.")
APIURL = f"https://opentdb.com/api.php?amount={NUM_OF_QUESTIONS}&category={EDUCATION_CATEGORY_ID}&type=multiple"
def geq():
    rsp = rqs.get(APIURL)
    if rsp.status_code == 200:
        d = rsp.json()
        if d["response_code"] == 0 and d["results"]:
            return d["results"]
    return None
def get_cat():
    return {c["id"]: c["name"] for c in rqs.get("https://opentdb.com/api_category.php").json()["trivia_categories"]}
def rq():
    global EDUCATION_CATEGORY_ID
    qts = geq()
    if not qts:
        print("Failed to fetch educational questions.")
        return
    s = 0
    print("Welcome to the Education Quiz!\n")
    cat = get_cat()
    print(f"\nTopic : {cat[EDUCATION_CATEGORY_ID]}")
    start_time = t.time()
    for i,q in enumerate(qts,1):
        global time_up
        time_up = False
        timer = thr.Thread(target = countdown,args = (10,))
        timer.start()
        qt = html.unescape(q["question"])
        crt = html.unescape(q["correct_answer"])
        icrt = [html.unescape(fa) for fa in q["incorrect_answers"]]
        o = icrt + [crt]
        rd.shuffle(o)
        print(f"Question {i}. {qt}")
        for idx,opt in enumerate(o,1):
            print(f"   {idx}. {opt}")
        while 1:
            try:
                choice = int(input("\nYour answer (1 - 4) : "))
                if 1 <= choice <= 4:
                    time_up = True
                    break
                else:
                    print("Invalid Input! Please enter 1-4")
            except ValueError:
                print("Invalid Input! Please enter a number")
        timer.join()
        if choice == None:
            print(f"\n⏰ You didn't answer the question in time. Correct answer : {crt}\n")
        elif o[choice - 1] == crt:
            print("✔️ Correct!\n")
            s += 1
        else:
            print(f"❌ Wrong! Correct answer : {crt}\n")
    end_time = t.time()
    total_time = int(end_time - start_time)
    print(f"Final Score : {s}/{len(qts)}")
    print(f"Percentage : {(s/len(qts)) * 100:.1f}%")
    print(f"⏱️ Total Time Taken : {total_time} seconds")
if __name__ == "__main__":
    rq()