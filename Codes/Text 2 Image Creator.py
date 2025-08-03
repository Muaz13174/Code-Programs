import requests as rqs
from PIL import Image as I
from io import BytesIO as BIO
from config import MONSTER_API_KEY as MAK
apit = MAK
print("Welcome to AI Art Buddy 🖼️!")
ui = input("Enter a description for the image :\n -> ")
url = r"https://api.monsterapi.ai/v1/generate/txt2img"
headers = {"Authorization":f"Bearer {apit}"}
rsp = rqs.post(url,headers = headers,json = {"prompt" : ui,"safe_filter" : True})
if rsp.status_code == 200:
    print("Loading...The image may take a few seconds.")
    prcid = rsp.json().get("process_id")
    while True:
        sttsdt = rqs.get(f"https://api.monsterapi.ai/v1/status/{prcid}",headers = headers).json()
        stts = sttsdt.get("status")
        if stts == "COMPLETED":
            imgurl = sttsdt["result"]["output"][0]
            img = I.open(BIO(rqs.get(imgurl).content))
            img.show()
            print()
            break
        elif stts == "FAILED":
            print("Image Generation Failed.")
            break
else:
    print(f"Error {rsp.status_code}")