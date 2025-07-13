import requests as rqs
import random as rd
import html
import time as t
import threading as thr
import winsound as ws
import msvcrt as msv
import sys
import select
def get_answer_with_timer(seconds = 10):
    bar_length = 20
    start = t.time()
    while True:
        elapsed = t.time() - start
        remaining = seconds - elapsed
        if remaining <= 0:
            print("\r⏰ Time's up!          ")
            ws.Beep(1000, 500)
            return None
        filled = int(bar_length * (remaining / seconds))
        bar = "#" * filled + "-" * (bar_length - filled)
        print(f"\r⏳ Time left: [{bar}] {int(remaining)}s", end="", flush=True)
        if sys.stdin in select.select([sys.stdin], [], [], 1)[0]:
            answer = sys.stdin.readline().strip()
            return answer
EDUCATION_CATEGORY_ID = rd.randint(9,32)
NUM_OF_QUESTIONS = 10
while 1:
    try:
        user_input = int(input("📝 How many questions would you like (5-50)? "))
        if 5 <= user_input <= 50:
            NUM_OF_QUESTIONS = user_input
            break
        else:
            print("⚠️ Please enter a number between 5 and 50.\n")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.\n")
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
        qt = html.unescape(q["question"])
        crt = html.unescape(q["correct_answer"])
        icrt = [html.unescape(fa) for fa in q["incorrect_answers"]]
        o = icrt + [crt]
        rd.shuffle(o)
        print(f"\nQuestion {i}. {qt}")
        for idx,opt in enumerate(o,1):
            print(f"   {idx}. {opt}")
        choice = None
        while True:
            ans = get_answer_with_timer()
            if ans is None:
                print(f"\n⏰ You didn't answer the question in time. Correct answer : {crt}\n")
                break
            if ans.isdigit() and 1 <= int(ans) <= 4:
                choice = int(ans)
                break
            else:
                print("Invalid Input! Please enter 1-4")
        if choice is not None:
            if o[choice - 1] == crt:
                print("✔️ Correct!\n")
                s += 1
            else:
                print(f"❌ Wrong! Correct answer : {crt}\n")
    end_time = t.time()
    total_time = int(end_time - start_time)
    print("\n🎉 Quiz Complete!")
    print(f"✅ Final Score     : {s}/{len(qts)}")
    print(f"📊 Percentage      : {(s / len(qts)) * 100:.1f}%")
    print(f"⏱️  Total Time Taken : {total_time} seconds")
if __name__ == "__main__":
    rq()