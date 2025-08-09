import requests as rqs
from PIL import Image as I
from io import BytesIO as BIO
from config import HP_API_KEY as HAK
def gnrtinpntngimg(prompt,imgp,mp):
    APIURL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-inpainting"
    hdrs = {"Authorization":f"Bearer {HAK}"}
    with open(imgp,"rb") as imgf:
        imgd = imgf.read()
    with open(mp,"rb") as mf:
        md = mf.read()
    pyld = {"inputs":prompt}
    files = {
        "image":("image.png",imgd,"image/png"),
        "mask":("mask.png",md,"image/png")
    }
    rsp = rqs.post(APIURL,pyld,headers = hdrs,files = files)
    if rsp.status_code == 200:
        return I.open(BIO(rsp.content))
    else:
        raise Exception(f"Request failed with status code {rsp.status_code}:{rsp.text}")
def main():
    print("Welcome to the Inpainting and Restoration Challenge!\nThis activity allows you to restore or transform parts of an existing image.\nProvide a base image, a mask indicating the areas to modify, and a text prompt describing the desired change.\nType \"exit\" or \"quit\" at any prompt to quit.\n")
    while 1:
        prompt = input("Enter a description for the inpainting (or \"exit\"/\"quit\" to quit) :\n -> ")
        if prompt.lower() in ["exit","quit"]:
            print("Goodbye!")
            break
        imgp = input("Enter the path to the base image (e.g., base_image.png) :\n -> ")
        if imgp.lower() in ["exit","quit"]:
            break
        mp = input("Enter the path to the mask image (e.g., mask_image.png) :\n -> ")
        if mp.lower() in ["exit","quit"]:
            break
        try:
            print("\nProcessing inpainting...")
            rstimg = gnrtinpntngimg(prompt,imgp,mp)
            rstimg.show()
            so = input("Do you want to save the inpainted image? (yes/no) :\n -> ")
            if so.lower() == "yes":
                fn = input("Enter a name for the image file (without extension) :\n -> ").strip()
                rstimg.save(f"{fn}.png")
                print(f"Image saved as {fn}.png\n")
            print("-" * 80 + "\n")
        except Exception as e:
            print(f"An error occured : {e}\n")
if __name__ == "__main__":
    main()