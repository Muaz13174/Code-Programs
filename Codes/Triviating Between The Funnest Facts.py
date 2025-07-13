import requests as rqs
import random as rd
import html
EDUCATION_CATEGORY_ID = rd.randint(9,32)
APIURL = f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"
def geq():
    rsp = rqs.get(APIURL)
    if rsp.status_code == 200:
        d = rsp.json()
        if d["response_code"] == 0 and d["results"]:
            return d["results"]
    return None
def rq():
    qts = geq()
    if not qts:
        print("Failed to fetch educational questions.")
        return
    s = 0
    print("Welcome to the Education Quiz!\n")
    for i,q in enumerate(qts,1):
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
                    break
            except ValueError:
                pass
            print("Invalid Input! Please enter 1-4")
        if o[choice - 1] == crt:
            print("✔️ Correct!\n")
            s += 1
        else:
            print(f"❌ Wrong! Correct answer : {crt}\n")
    print(f"Final Score : {s}/{len(qts)}")
    print(f"Percentage : {(s/len(qts)) * 100:.1f}%")
if __name__ == "__main__":
    rq()