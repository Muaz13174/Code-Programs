import requests as rqs
def grj():
    url = r"https://official-joke-api.appspot.com/random_joke"
    rsp = rqs.get(url)
    if rsp.status_code == 200:
        print(f"Full JSON Response : {rsp.json()}")
        jd = rsp.json()
        #print(jd)
        return f"{jd['setup']} - {jd['punchline']}"
    else:
        return "Failed to read joke"
def main():
    print("Welcome to the Random Joke Generator!!!")
    while 1:
        ui = input("Press Enter to get a new joke, or type q/exit to quit : ").strip().lower()
        if ui in ["q","exit"]:
            print("Goodbye!")
            return
        j = grj()
        print(j)
if __name__ == "__main__":
    main()