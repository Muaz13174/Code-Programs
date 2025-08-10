import requests as rqs
from config import HP_API_KEY as HAK
MODELID = "nlpconnect/vit-gpt2-image-captioning"
APIURL = fr"https://api-inference.huggingface.co/models/{MODELID}"
hdrs = {"Authorization":f"Bearer {HAK}"}
def cptnsnglimg():
    import os
    imgsrc = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","Pictures","test pic.jpg")
    try:
        with open(imgsrc,"rb") as o:
            imgbytes = o.read()
    except Exception as e:
        print(f"Could not load image from {imgsrc}.\nError : {e}")
        return
    rsp = rqs.post(url = APIURL,headers = hdrs,data = imgbytes)
    rslt = rsp.json()
    if isinstance(rslt,dict) and "error" in rslt:
        print(f"[Error] {rslt['error']}")
        return
    cptn = rslt[0].get("generated_text","No caption found.")
    print(f"Image : {imgsrc}")
    print(f"Caption : {cptn}")
if __name__ == "__main__":
    cptnsnglimg()