import requests as rqs
from config import HP_API_KEY
def ct(t):
    APIURL = r"https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    hdrs = {"Authorization":f"Bearer {HP_API_KEY}"}
    pyld = {"inputs":t}
    rsp = rqs.get(APIURL,headers = hdrs,json = pyld)
    if rsp.status_code == 200:
        cls = rsp.json()
        print(f"Predicted Label : {cls[0]['label']}")
    else:
        print(f"Error {rsp.status_code}")
if __name__ == "__main__":
    st = "I love using HuggingFace API!"
    ct(st)