from config import HP_API_KEY as HAK
import requests as rqs
from PIL import Image as I
import io
import os
from colorama import init
from colorama import Fore as F
from colorama import Style as S
import json
init(autoreset = True)
def qhfapi(apiurl,pyld = None,files = None,method = "post"):
    hdrs = {"Authorization":f"Bearer {HAK}"}
    try:
        if method.lower() == "post":
            rsp = rqs.post(apiurl,headers = hdrs,json = pyld,files = files)
        else:
            rsp = rqs.get(apiurl,headers = hdrs,params = pyld)
        if rsp.status_code != 200:
            raise Exception(f"Status {rsp.status_code} : {rsp.text}")
        return rsp.content
    except Exception as e:
        print(F.RED + f"❌ Error while calling API : {e}")
        raise
def gtbsccptn(img,model = "nlpconnect/vit-gpt2-image-captioning"):
    print(f"{F.YELLOW}????? Generating basic caption using vit-gpt2-image-captioning...")
    apiurl = fr"https://api-inference.huggingface.co/models/{model}"
    buffered = io.BytesIO()
    img.save(buffered,format = "JPEG")
    buffered.seek(0)
    