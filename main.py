from datetime import datetime
import requests
from bs4 import BeautifulSoup

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")
payload = {"date_req": today}

response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, "html.parser")

def GetCurse(id):
    return xml.find("valute", {'id': id}).value.text.replace(",",".")

def get_convert(valute_from, valute_to, amont):
    all_charcodes = xml.find_all("valute")
    value_from = 0
    value_to = 0
    for char_code in all_charcodes:
        if valute_from == char_code.charcode.text:
            value_from = char_code.value.text
        elif valute_to == char_code.charcode.text:
            value_to = char_code.value.text

    value_to = float(value_to.replace(",","."))
    value_from = float(value_from.replace(",","."))
    result = (amont * value_from) / value_to
    return round(result,2)
print(get_convert("VND","HKD",4))



