import requests as rqs
from config import HP_API_KEY as HAK
from PIL import Image as I
from transformers import BlipProcessor as BP
from transformers import BlipForConditionalGeneration as BFCG
# The "Not Working" Code
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
# The "Working" Code
def theworkingcptnsnglimg():
    imgurl = r"https://tse3.mm.bing.net/th/id/OIP.uHaqRdiMzWSMCR2LzsmhtQHaEZ?pid=Api&p=0&h=180"
    img = I.open(rqs.get(imgurl,stream = True).raw)
    processer = BP.from_pretrained("Salesforce/blip-image-captioning-base")
    mdl = BFCG.from_pretrained("Salesforce/blip-image-captioning-base")
    ipts = processer(images = img,return_tensors = "pt")
    otpt = mdl.generate(**ipts)
    cptn = processer.decode(otpt[0],skip_special_tokens = True)
    print(f"Image Description : {cptn}")
if __name__ == "__main__":
    #cptnsnglimg()
    #print("\n")
    theworkingcptnsnglimg()