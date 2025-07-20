import requests as rqs
from config import HP_API_KEY
def ct(t):
    APIURL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
    hdrs = {"Authorization":f"Bearer {HP_API_KEY}"}
    pyld = {"inputs":t}
    return rqs.get(APIURL,headers = hdrs,json = pyld).json()
if __name__ == "__main__":
    st = "I love using HuggingFace API!"
    print(ct(st))