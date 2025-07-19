import requests as rqs
url = r"https://uselessfacts.jsph.pl/random.json?language=en"
def grtf():
    rsp = rqs.get(url)
    if rsp.status_code == 200:
        fd = rsp.json()
        print(f"Did you know? {fd['text']}")
    else:
        print("Failed to fetch fact")
while 1:
    ui = input("Press the Enter key to get a random technology fact or type \"q\" to quit...")
    if ui.lower() == "q":
        break
    grtf()