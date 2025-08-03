from PIL import Image as I
from PIL import ImageEnhance as IMGENH
from PIL import ImageFilter as IMGFIL
import requests as rqs
from io import BytesIO as BIO
from config import HP_API_KEY as HAK
def gift(prompt : str) -> I.Image:
    API_URL = r"https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
    headers = {"Authorization":f"Bearer {HAK}"}
    payload = {"inputs":prompt}
    rsp = rqs.post(API_URL,headers = headers,json = payload,timeout = 30)
    if rsp.status_code == 200:
        img = I.open(BIO(rsp.content))
        return img
    else:
        raise Exception(f"Request failed with status code {rsp.status_code}:{rsp.text}")
def dlfx(img):
    img = IMGENH.Brightness(img).enhance(1.3)
    img = IMGENH.Contrast(img).enhance(1.1)
    img = img.filter(IMGFIL.GaussianBlur(1))
    return img
def nmfx(img):
    img = IMGENH.Brightness(img).enhance(0.9)
    img = IMGENH.Contrast(img).enhance(1.4)
    img = img.filter(IMGFIL.GaussianBlur(0.5))
    return img
def main():
    print("Welcome to the AI Image Stylist Project!")
    prompt = input("Enter your image description :\n -> ").strip()
    try:
        print("Generating your base image...\n")
        img = gift(prompt)
        print("Applying Daylight Edition Style...")
        dimg = dlfx(img)
        dimg.show()
        dimg.save(f"{prompt.replace(" ","_")}_daylight.png")
        print("Daylight Edition Saved.\n")
        print("Applying Night Mood Style...")
        nimg = nmfx(img)
        nimg.show()
        nimg.save(f"{prompt.replace(" ","_")}_night.png")
        print("Night Mood Saved.\n")
    except Exception as e:
        print(f"Something went wrong : {e}")
if __name__ == "__main__":
    main()