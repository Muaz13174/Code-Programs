import tkinter as tk
from tkinter import scrolledtext as scrldtxt
from transformers import pipeline as ppln
import requests as rqs
from config import UCLASSIFY_API_KEY as UCLAK
summarizer = ppln("summarization","facebook/bart-large-cnn")
UCLURL = r"https://api.uclassify.com/v1/uClassify/Topics/classify"
def smrztxt(txt):
    smry = summarizer(txt,max_length = 100,min_length = 30,do_sample = False)
    return smry[0]["summary_text"]
def clsfysmry(smry):
    hdrs = {
        "Authorization":f"Token {UCLAK}",
        "Content-Type":"application/json"
    }
    dt = {
        "texts":smry
    }
    rsp = rqs.post(UCLURL,headers = hdrs,json = dt)
    rslts = rsp.json()[0]["classification"]
    return "\n".join([f"{item['className']}:{item['p']:.2f}" for item in rslts])
def prcstxt():
    input_text = text_input.get("1.0",tk.END).strip()
    if not input_text:
        output_summary.delete("1.0",tk.END)
        output_summary.insert(tk.END,"Please enter some text.")
        return
    smry = smrztxt(input_text)
    clsfctn = clsfysmry(smry)
    output_summary.delete("1.0",tk.END)
    output_summary.insert(tk.END,f"📝 Summary :\n{smry}\n\n🔍 Classification :\n{clsfctn}")
root = tk.Tk()
root.title("Text Summarizer & Classifier")
tk.Label(root,text = "Enter your text : ").pack()
text_input = scrldtxt.ScrolledText(root,wrap = tk.WORD,width = 60,height = 10)
text_input.pack(padx = 10,pady = 5)
tk.Button(root,text = "Summarize & Classifiy",command = prcstxt).pack(pady = 10)
output_summary = scrldtxt.ScrolledText(root,wrap = tk.WORD,width = 60,height = 15)
output_summary.pack(padx = 10,pady = 5)
root.mainloop()