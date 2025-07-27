import requests as rqs
from colorama import init
from colorama import Fore as f
from colorama import Style as s
init(True)
def sumtext(text):
    print(f.YELLOW + "\n🔍 Summarizing your text...")
    url = r"https://api.smmry.com"
    params = {
        "SM_API_INPUT":text,
        "SM_LENGTH":3
    }
    try:
        rsp = rqs.post(url,params)
        rslt = rsp.json()
        if "sm_api_content" in rslt:
            summary = rslt["sm_api_content"]
            print(f.CYAN + "\n📝 Summary :\n" + f.GREEN + summary)
        else:
            print(f.RED + "\n❌ Error :",rslt.get("sm_api_message","Unexpected response."))
    except Exception as e:
        print(f.RED + f"\n❌ Request Failed : {e}")
    
text = "Computers are powerful electronic devices that process and store information, making them essential tools in modern life. They can perform a wide range of tasks, from simple calculations to complex data analysis, through the use of hardware components like processors, memory, and storage, and software such as operating systems and applications. Computers have revolutionized industries such as education, healthcare, finance, and entertainment by increasing efficiency and enabling new possibilities for communication and innovation. With ongoing advancements in technology, computers continue to evolve, becoming faster, more compact, and increasingly integrated into everyday life."
sumtext(text)