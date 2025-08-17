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
    hdrs = {"Authorization":f"Bearer {HAK}"}
    rsp = rqs.post(apiurl,headers = hdrs,data = buffered.read())
    rslt = rsp.json()
    if isinstance(rslt,dict) and "error" in rslt:
        return f"[Error] {rslt['error']}"
    cptn = rslt[0].get("generated_text","No caption generated.")
    return cptn
def gnrttxt(prompt,model = "gpt2",max_new_tokens = 60):
    print(f"{F.CYAN}????? Generating text with prompt : {prompt}")
    apiurl = fr"https://api-inference.huggingface.co/models/{model}"
    pyld = {"inputs" : prompt,"parameters" : {"max_new_tokens" : max_new_tokens}}
    txtbts = qhfapi(apiurl,pyld)
    try:
        rslt = json.loads(txtbts.decode("utf-8"))
    except Exception as e:
        raise Exception("Failed to decode text generation response.")
    if isinstance(rslt,dict) and "error" in rslt:
        raise Exception(rslt["error"])
    generated = rslt[0].get("generated_text","")
    return generated
def trncttxt(txt,wrdlmt):
    wrds = txt.strip().split()
    return " ".join(wrds[:wrdlmt])
def print_menu():
    print(f"""{S.BRIGHT}
{F.GREEN}================ Image-to-Text Conversion =================
Select Output Type :
1. Caption (5 words)
2. Description (30 words)
3. Summary (50 words)
4. Exit
===============================================================
""")
    return
def main():
    imgpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","Pictures","test pic.jpg")
    try:
        img = I.open(imgpath)
    except Exception as e:
        print(f"{F.RED}❌ Failed to open image : {e}")
        return
    bsccptn = gtbsccptn(img)
    print(f"{F.YELLOW}????? Basic Caption : {S.BRIGHT}{bsccptn}\n")
    while True:
        print_menu()
        choice = str(input(f"{F.CYAN}Enter your choice (1 - 4) : {S.RESET_ALL}"))
        if choice == "1":
            cptn = trncttxt(bsccptn,5)
            print(f"{F.GREEN}✅ Caption (5 words) : {S.BRIGHT}{cptn}\n")
        elif choice == "2":
            prompttxt = f"Expand the following caption into a detailed description in exactly 30 words : {bsccptn}"
            try:
                generated = gnrttxt(prompttxt,max_new_tokens = 40)
                description = trncttxt(generated,30)
                print(f"{F.GREEN}✅ Description (30 words) : {S.BRIGHT}{description}\n")
            except Exception as e:
                print(f"{F.RED}❌ Failed to generate description : {e}")
        elif choice == 3:
            prompttxt = f"Summarize the content of the image described by this caption into a summary of exactly 50 words : {bsccptn}"
            try:
                generated = gnrttxt(prompttxt)
                summary = trncttxt(generated,50)
                print(f"{F.GREEN}✅ Summary (50 words) : {S.BRIGHT}{summary}\n")
            except Exception as e:
                print(f"{F.RED}❌ Failed to generate summary : {e}")
        elif choice == "4":
            print(f"{F.GREEN}????? Goodbye!")
            return
        else:
            print(f"{F.RED}❌ Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()