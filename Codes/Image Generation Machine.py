import requests as rqs
from PIL import Image as I
from io import BytesIO as BIO
from config import HP_API_KEY as HAK
API_URL = r"https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
def gift(prompt : str) -> I.Image:
    headers = {"Authorization":f"Bearer {HAK}"}
    payload = {"inputs":prompt}
    try:
        rsp = rqs.post(API_URL,headers = headers,json = payload,timeout = 30)
        rsp.raise_for_status()
        if "image" in rsp.headers.get("Content-Type",""):
            img = I.open(BIO(rsp.content))
            return img
        else:
            raise Exception("The response is not an image. It might be an error message.")
    except rqs.exceptions.RequestException as e:
        raise Exception(f"Request Failed : {e}")
def main():
    print("Welcome to the Text-To-Image Generator!\nType \"exit\" to quit the program.\n")
    while 1:
        prompt = input("Enter a description for the image you want to generate : \n -> ")
        if prompt.lower() == "exit":
            print("Goodbye!") ; break
        print("\nGenerating Image...\n")
        try:
            img = gift(prompt)
            img.show()
            save_option = input("Do you want to save this image? : ").strip().lower()
            if save_option == "yes":
                fn = input("Enter a name (without the file extension) : ").strip() or "generated_image"
                fn = "".join(c for c in fn if c.isalnum() or c in ("_","-")).rstrip()
                img.save(f"{fn}.png")
                print(f"Image saved as \"{fn}.png\"")
        except Exception as e:
            print(f"An error occured : {e}\n")
        print("-"*80 + "\n")
if __name__ == "__main__":
    main()