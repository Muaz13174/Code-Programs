import re
import random as r
from colorama import Fore as f
from colorama import Style as s
from colorama import init as i
from time import localtime as t
from time import strftime as tstr
from pytz import timezone as tz
from datetime import datetime as dt
i(autoreset = True)
wi = {
    "hot":["United Arab Emirates","Singapore","Cyprus"],
    "deciduous":["United States of America","Southern Chile","Japan"],
    "cold":["Canada","Norway","Russia"]
}
nu = [
    f"{f.LIGHTCYAN_EX}A Drought In Mexico Kills 200 people{s.RESET_ALL}",
    f"{f.LIGHTCYAN_EX}Hurricane Connie Hits Florida!{s.RESET_ALL}",
    f"{f.LIGHTCYAN_EX}Heavy Monsoons Causes Floods In Bangladesh{s.RESET_ALL}"
]
lt = [
    ["Cambodia","Asia/Phnom_Penh"],
    ["India","Asia/Kolkata"],
    ["Usa","America/New_York"],
    ["Russia","Europe/Moscow"],
    ["France","Europe/Paris"],
    ["Germany","Europe/Berlin"],
    ["United Kingdom","Europe/London"],
    ["Uk","Europe/London"],
    ["Great Britain","Europe/London"],
    ["British Isles","Europe/London"],
    ["Spain","Europe/Madrid"],
    ["Portugal","Europe/Lisbon"],
    ["Bosnia And Herzegovina","Europe/Sarajevo"],
    ["Brazil","America/Sao_Paulo"],
    ["Argentina","America/Argentina/Buenos_Aires"],
    ["Venezuela","America/Caracas"],
    ["Lesotho","Africa/Maseru"],
    ["South Africa","Africa/Johannesburg"],
    ["Afghanistan","Asia/Kabul"],
    ["Namibia","Africa/Windhoek"],
    ["Mauritius","Indian/Mauritius"],
    ["Korea","Asia/Seoul"],
    ["Mexico","America/Mexico_City"],
    ["Antigua And Barbuda","America/Antigua"],
    ["Algeria","Africa/Algiers"],
    ["Andorra","Europe/Andorra"],
    ["Albania","Europe/Tirane"],
    ["Angola","Africa/Luanda"],
    ["Armenia","Asia/Yerevan"],
    ["Aruba","America/Aruba"],
    ["Australia","Australia/Sydney"],
    ["Austria","Europe/Vienna"],
    ["Azerbaijan","Asia/Baku"],
    ["Bahamas","America/Nassau"],
    ["Bahrain","Asia/Bahrain"],
    ["Bangladesh","Asia/Dhaka"],
    ["Barbados","America/Barbados"],
    ["Belarus","Europe/Minsk"],
    ["Belgium","Europe/Brussels"],
    ["Belize","America/Belize"],
    ["Benin","Africa/Porto-Novo"],
    ["Bermuda","Atlantic/Bermuda"],
    ["Bhutan","Asia/Thimphu"],
    ["Bolivia","America/La_Paz"],
    ["Botswana","Africa/Gaborone"],
    ["Brunei","Asia/Brunei"],
    ["Bulgaria","Europe/Sofia"],
    ["Burkina Faso","Africa/Ouagadougou"],
    ["Burundi","Africa/Bujumbura"],
    ["Cape Verde","Atlantic/Cape_Verde"],
    ["Cabo Verde","Atlantic/Cape_Verde"],
    ["Cameroon","Africa/Douala"],
    ["Canada","America/Toronto"],
    ["Central African Republic","Africa/Bangui"],
    ["Chad","Africa/Ndjamena"],
    ["Chile","America/Santiago"],
    ["China","Asia/Shanghai"],
    ["Colombia","America/Bogota"],
    ["Comoros","Indian/Comoro"],
    ["Democratic Republic Of The Congo","Africa/Kinshasa"],
    ["DRC","Africa/Kinshasa"],
    ["Republic Of The Congo","Africa/Brazzaville"],
    ["Costa Rica","America/Costa_Rica"],
    ["Côte D'Ivoire","Africa/Abidjan"],
    ["Ivory Coast","Africa/Abidjan"],
    ["Croatia","Europe/Zagreb"],
    ["Cuba","America/Havana"],
    ["Curaçao","America/Curacao"],
    ["Curacao","America/Curacao"],
    ["Cyprus","Asia/Nicosia"],
    ["Czech Republic","Europe/Prague"],
    ["Denmark","Europe/Copenhagen"],
    ["Djibouti","Africa/Djibouti"],
    ["Dominica","America/Dominica"],
    ["Dominican Republic","America/Santo_Domingo"],
    ["East Timor","Asia/Dili"],
    ["Timor-Leste","Asia/Dili"],
    ["Timor Leste","Asia/Dili"],
    ["Ecuador","America/Guayaquil"],
    ["Egypt","America/Guayaquil"],
    ["El Salvador","America/El_Salvador"],
    ["Equatorial Guinea","Africa/Malabo"],
    ["Eritrea","Africa/Asmara"],
    ["Estonia","Europe/Tallinn"],
    ["Eswatini","Africa/Mbabane"],
    ["Swaziland","Africa/Mbabane"],
    ["Ethiopia","Africa/Addis_Ababa"],
    ["Fiji","Pacific/Fiji"],
    ["Finland","Europe/Helsinki"],
    ["French Polynesia","Pacific/Tahiti"],
    ["Gabon","Africa/Libreville"],
    ["Gambia","Africa/Banjul"],
    ["Georgia","Asia/Tbilisi"],
    ["Ghana","Africa/Accra"],
    ["Greece","Europe/Athens"],
    ["Grenada","America/Grenada"],
    ["Guatemala","America/Guatemala"],
    ["Guinea","Africa/Conakry"],
    ["Guinea-Bissau","Africa/Bissau"],
    ["Guinea Bissau","Africa/Bissau"],
    ["Guyana","America/Guyana"],
    ["Haiti","America/Port-au-Prince"],
    ["Honduras","America/Tegucigalpa"],
    ["Hungary","Europe/Budapest"],
    ["Iceland","Atlantic/Reykjavik"],
    ["Indonesia","Asia/Jakarta"],
    ["Iran","Asia/Tehran"],
    ["Iraq","Asia/Baghdad"],
    ["Ireland","Europe/Dublin"],
    ["Israel","Asia/Jerusalem"],
    ["Italy","Europe/Rome"],
    ["Jamaica","America/Jamaica"],
    ["Japan","Asia/Tokyo"],
    ["Jordan","Asia/Amman"],
    ["Kazakhstan","Asia/Almaty"],
    ["Kenya","Africa/Nairobi"],
    ["Kiribati","Pacific/Tarawa"],
    ["Kuwait","Asia/Kuwait"],
    ["Kyrgyzstan","Asia/Bishkek"],
    ["Laos","Asia/Vientiane"],
    ["Latvia","Europe/Riga"],
    ["Lebanon","Asia/Beirut"],
    ["Liberia","Africa/Monrovia"],
    ["Libya","Africa/Tripoli"],
    ["Liechtenstein","Europe/Vaduz"],
    ["Lithuania","Europe/Vilnius"],
    ["Luxembourg","Europe/Luxembourg"],
    ["Madagascar","Indian/Antananarivo"],
    ["Malawi","Africa/Blantyre"],
    ["Malaysia","Asia/Kuala_Lumpur"],
    ["Maldives","Indian/Maldives"],
    ["Mali","Africa/Bamako"],
    ["Malta","Europe/Malta"],
    ["Marshall Islands","Pacific/Majuro"],
    ["Mauritania","Africa/Nouakchott"],
    ["Micronesia","Pacific/Pohnpei"],
    ["Moldova","Europe/Chisinau"],
    ["Monaco","Europe/Monaco"],
    ["Mongolia","Asia/Ulaanbaatar"],
    ["Montenegro","Europe/Podgorica"],
    ["Morocco","Africa/Casablanca"],
    ["Mozambique","Africa/Maputo"],
    ["Myanmar","Asia/Yangon"],
    ["Burma","Asia/Yangon"],
    ["Nauru","Pacific/Nauru"],
    ["Nepal","Asia/Kathmandu"],
    ["Netherlands","Europe/Amsterdam"],
    ["New Zealand","Pacific/Auckland"],
    ["Nicaragua","America/Managua"],
    ["Niger","Africa/Niamey"],
    ["Nigeria","Africa/Lagos"],
    ["North Macedonia","Europe/Skopje"],
    ["Norway","Europe/Oslo"],
    ["Oman","Asia/Muscat"],
    ["Pakistan","Asia/Karachi"],
    ["Palau","Pacific/Palau"],
    ["Panama","America/Panama"],
    ["Papua New Guinea","Pacific/Port_Moresby"],
    ["Paraguay","America/Asuncion"],
    ["Peru","America/Lima"],
    ["Philippines","Asia/Manila"],
    ["Poland","Europe/Warsaw"],
    ["Qatar","Asia/Qatar"],
    ["Romania","Europe/Bucharest"],
    ["Rwanda","Africa/Kigali"],
    ["Saint Kitts And Nevis","America/St_Kitts"],
    ["Saint Lucia","America/St_Lucia"],
    ["Saint Vincent And The Grenadines","America/St_Vincent"],
    ["Samoa","Pacific/Apia"],
    ["San Marino","Europe/San_Marino"],
    ["São Tomé And Príncipe","Africa/Sao_Tome"],
    ["Sao Tome And Principe","Africa/Sao_Tome"],
    ["Saudi Arabia","Asia/Riyadh"],
    ["Senegal","Africa/Dakar"],
    ["Serbia","Europe/Belgrade"],
    ["Seychelles","Indian/Mahe"],
    ["Sierra Leone","Africa/Freetown"],
    ["Singapore","Asia/Singapore"],
    ["Slovakia","Europe/Bratislava"],
    ["Slovenia","Europe/Ljubljana"],
    ["Solomon Islands","Pacific/Guadalcanal"],
    ["Somalia","Africa/Mogadishu"],
    ["Sri Lanka","Asia/Colombo"],
    ["Sudan","Africa/Khartoum"],
    ["South Sudan","Africa/Juba"],
    ["Suriname","America/Paramaribo"],
    ["Sweden","Europe/Stockholm"],
    ["Switzerland","Europe/Zurich"],
    ["Syria","Asia/Damascus"],
    ["Taiwan","Asia/Taipei"],
    ["Tajikistan","Asia/Dushanbe"],
    ["Tanzania","Africa/Dodoma"],
    ["Thailand","Asia/Bangkok"],
    ["Togo","Africa/Lome"],
    ["Tonga","Pacific/Tongatapu"],
    ["Trinidad And Tobago","America/Port_of_Spain"],
    ["Tunisia","Africa/Tunis"],
    ["Turkey","Europe/Istanbul"],
    ["Turkmenistan","Asia/Ashgabat"],
    ["Tuvalu","Pacific/Funafuti"],
    ["Uganda","Africa/Kampala"],
    ["Ukraine","Europe/Kiev"],
    ["United Arab Emirates","Asia/Dubai"],
    ["Uae","Asia/Dubai"],
    ["Uruguay","America/Montevideo"],
    ["Uzbekistan","Asia/Tashkent"],
    ["Vanuatu","Pacific/Efate"],
    ["Vatican City","Europe/Vatican"],
    ["Vietnam","Asia/Ho_Chi_Minh"],
    ["Yemen","Asia/Aden"],
    ["Zambia","Africa/Lusaka"],
    ["Zimbabwe","Africa/Harare"]
]
def t(c):
    c = c.lower().title()
    l = 0
    for i in lt:
        l += 1
        if i[0] == c:
            return [i[0],dt.now(tz(i[1])).strftime("%I:%M:%S %p")]
    if l == 212:
        return ["No country!!!",l]
def sh():
    print(f"{f.MAGENTA}\nI can:{s.RESET_ALL}")
    print(f"{f.GREEN}- Show weather information (say 'weather')\n- Share the latest news updates (say 'news')\n- Express local time in different cities (say 'local time'){s.RESET_ALL}")
    print(f"{f.CYAN}Type 'exit' or 'bye' to end.{s.RESET_ALL}\n")
def ni(t):
    return re.sub(r"\s+"," ",t.strip().lower())
def swi():
    print(f"{f.CYAN}WeatherBot : hot, deciduous, or cold climate?")
    global p
    p = str(input(f"{f.YELLOW}You : "))
    p = ni(p)
    if p in wi:
        print(f"{f.GREEN}WeatherBot : {r.choice(wi[p])} has a {p} climate.{s.RESET_ALL}")
    else:
        print(f"{f.RED}WeatherBot : Sorry, I don't have that type of climate.{s.RESET_ALL}")
    sh()
def stlnu():
    print(f"{f.YELLOW}Latest News!\n{f.LIGHTYELLOW_EX}    {r.choice(nu)}")
    sh()
def eltidc():
    print(f"{f.CYAN}WeatherBot : Type in any country in the world and I will provide you the local time at its capital.{s.RESET_ALL}")
    c = str(input(f"{f.YELLOW}You : "))
    time = t(c)
    if time[0] == "Usa":
        time[0] = "The USA"
    elif time[0] == "Bosnia And Herzegovina":
        time[0] = "Bosnia and Herzegovina"
    elif time[0] == "Antigua And Barbuda":
        time[0] = "Antigua and Barbuda"
    elif time[0] == "Bahamas":
        time[0] = "The Bahamas"
    elif time[0] == "Democratic Republic Of The Congo" or time[0] == "DRC":
        time[0] = "Democratic Republic of the Congo"
    elif time[0] == "Republic Of The Congo":
        time[0] = "Republic of the Congo"
    elif time[0] == "Cote D'Ivoire" or time[0] == "Ivory Coast":
        time[0] = "Côte d'Ivoire"
    elif time[0] == "Gambia":
        time[0] = "The Gambia"
    elif time[0] == "Curacao":
        time[0] = "Curaçao"
    elif time[0] == "Timor-Leste" or time[0] == "Timor Leste":
        time[0] = "East Timor"
    elif time[0] == "Swaziland":
        time[0] = "Eswatini"
    elif time[0] == "Guinea Bissau":
        time[0] = "Guinea-Bissau"
    elif time[0] == "Burma":
        time[0] = "Myanmar"
    elif time[0] == "Saint Kitts And Nevis":
        time[0] = "Saint Kitts and Nevis"
    elif time[0] == "Saint Vincent And the Grenadines":
        time[0] = "Saint Vincent and the Grenadines"
    elif time[0] == "Sao Tome and Principe":
        time[0] = "São Tomé and Príncipe"
    elif time[0] == "Trinidad And Tobago":
        time[0] = "Trinidad and Tobago"
    elif time[0] == "Uk" or time[0] == "Great Britain" or time[0] == "British Isles":
        time[0] = "United Kingdom"
    elif time[0] == "Uae":
        time[0] = "United Arab Emirates"
    return [time[0],time[1]]
def c():
    print(f"{f.CYAN}Hello! I'm TravelBot.{s.RESET_ALL}")
    n = str(input(f"{f.YELLOW}Your name? :{s.RESET_ALL} "))
    print(f"{f.GREEN}Nice to meet you, {n}!{s.RESET_ALL}")
    sh()
    while True:
        ui = ni(str(input(f"{f.YELLOW}{n} :{s.RESET_ALL} ")))
        if "weather" in ui or "weather information" in ui:
            swi()
        elif "news" in ui or "updates" in ui or "news updates" in ui:
            stlnu()
        elif "time" in ui or "local time" in ui:
            tm = eltidc()
            if tm[1] != 212:
                print(f"{f.CYAN}WeatherBot : The local time in {f.GREEN}{tm[0]}{f.CYAN} is {f.BLUE}{tm[1]}{f.CYAN}.{s.RESET_ALL}")
            else:
                print(f"{f.RED}WeatherBot : Sorry, we don't have that country.{s.RESET_ALL}")
            sh()
        elif "help" in ui:
            sh()
        elif "exit" in ui or "bye" in ui:
            print(f"{f.CYAN}TravelBot : Safe travels! Goodbye!{s.RESET_ALL}")
            break
        else:
            print(f"{f.RED}TravelBot : Could you rephrase?{s.RESET_ALL}")
if __name__ == "__main__":
    c()