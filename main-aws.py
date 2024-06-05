import time
import re
from bs4 import BeautifulSoup as bs
import requests as req
import openpyxl
import random
from CPMy import arr
from requests_ip_rotator import ApiGateway

userAgents = [
"Mozilla/5.0 (iPod; CPU iPod OS 10_3_7; like Mac OS X) AppleWebKit/600.50 (KHTML, like Gecko) Chrome/51.0.1306.201 Mobile Safari/536.4",
"Mozilla/5.0 (Linux; U; Android 7.0; GT-I9200 Build/KTU84P) AppleWebKit/537.38 (KHTML, like Gecko) Chrome/51.0.1166.359 Mobile Safari/603.0",
"Mozilla/5.0 (Linux; Linux i684 x86_64; en-US) AppleWebKit/602.3 (KHTML, like Gecko) Chrome/49.0.1740.297 Safari/533",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_0; en-US) Gecko/20130401 Firefox/48.6",
"Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 6.3; x64 Trident/4.0)",
"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.3;; en-US Trident/4.0)",
"Mozilla/5.0 (Linux x86_64; en-US) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/52.0.2362.235 Safari/534",
"Mozilla/5.0 (iPad; CPU iPad OS 10_7_7 like Mac OS X) AppleWebKit/600.50 (KHTML, like Gecko) Chrome/48.0.3458.299 Mobile Safari/537.7",
"Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.0; WOW64; en-US Trident/7.0)",
"Mozilla/5.0 (Linux x86_64; en-US) Gecko/20100101 Firefox/46.5",
"Mozilla/5.0 (Windows; Windows NT 10.0; Win64; x64; en-US) AppleWebKit/602.18 (KHTML, like Gecko) Chrome/48.0.3174.208 Safari/534.4 Edge/17.14539",
"Mozilla/5.0 (Windows; U; Windows NT 6.0;; en-US) AppleWebKit/602.38 (KHTML, like Gecko) Chrome/51.0.3304.227 Safari/537",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_3_2; en-US) AppleWebKit/600.34 (KHTML, like Gecko) Chrome/54.0.3679.208 Safari/601",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 8_4_2; en-US) Gecko/20100101 Firefox/60.9",
"Mozilla/5.0 (Windows; U; Windows NT 10.4; Win64; x64; en-US) AppleWebKit/600.2 (KHTML, like Gecko) Chrome/48.0.2355.272 Safari/533.9 Edge/15.13715",
"Mozilla/5.0 (Windows; U; Windows NT 10.3;) AppleWebKit/603.26 (KHTML, like Gecko) Chrome/51.0.3008.352 Safari/535.0 Edge/9.23899",
"Mozilla/5.0 (Windows; U; Windows NT 10.0;) AppleWebKit/535.25 (KHTML, like Geckov) Chrome/55.0.2176.177 Safari/534.5 Edge/9.78105",
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_5; like Mac OS X) AppleWebKit/600.22 (KHTML, like Gecko) Chrome/48.0.1537.263 Mobile Safari/600.2",
"Mozilla/5.0 (Linux; U; Linux x86_64; en-US) Gecko/20100101 Firefox/54.7"
]

chromeDivs = [
    "MjjYud",
    "hlcw0c",
    "ULSxyf"
]

testUser = [

]

toSave = [
    
]

baseURL = "https://google.com/search?q="

def saveToExcel():
    wb = openpyxl.Workbook()
    ws = wb.active
    for tuples in toSave:
        ws.append([tuples[0], tuples[1], tuples[2], tuples[3], tuples[4], tuples[5], tuples[6], tuples[7], tuples[8], tuples[9]])
    wb.save("trademark_usage.xlsx")

def executeSearch(fname, lname, abbr, cert, sesh1, ide, date, email, emaily, phone, phoney):
    headers = {
        "User-Agent": random.choice(userAgents)
    }
    time.sleep(random.randint(2,5))
    status = 0
    retries = 0
    while status != 200:
        retries +=1
        if (retries % 6 == 0 and retries > 0):
            time.sleep(random.randint(10,15))
        try: 
            time.sleep(random.randint(1,3))
            response2 = sesh1.get(f'{baseURL}{fname}+{lname}+{cert}+{abbr}', headers=headers)
            status = response2.status_code
            print(status)
        except Exception as e:
            print(e)
            return False
    response2 = str(bs((response2.content), "html.parser"))
    match = re.search((fr"(?i)(?:{fname}\s*?.{{0,14}}?\s*?{lname}[\s\S]{{0,17}}?{abbr})"), response2)
    if (match):
        closest = 9999999999999
        try: 
            for tag in re.finditer(r'href=\"[\s\S]{110}', response2):
                b = match.start()
                c = (tag.start()) 
                a = b - c
                if a < closest and a > 0:
                    closest = a
                    href = tag
                elif a <= 0:
                    break
        except Exception as e:
            print(e)
        toSave.append([fname, lname, ide, href.group(), match.group(), date, email, emaily, phone, phoney])
        return True
    else:
        return False

def main():
    count=0
    gateway = ApiGateway("https://www.google.com/")
    gateway.start()
    sesh1 = req.Session()
    sesh1.mount("https://www.google.com/", gateway)
    for identity in arr:
        if (count % 75 == 0 and count > 1):
            print("Sleeping")
            time.sleep(random.randint(25,35))
        if (count % 175 == 0 and count > 1):
            print("Sleeping")
            time.sleep(random.randint(50,70))
        if (count % 500 == 0 and count > 1):
            saveToExcel()
        if (count % 750 == 0 and count > 1):
            print("Sleeping")
            time.sleep(random.randint(700,1000))
        count+= 1
        print(identity)
        returner = executeSearch(identity[0], identity[1], "CPM", "Certified Property Manager", sesh1, identity[2], identity[3], identity[4], identity[5], identity[6], identity[7])
        print(count, returner)
    saveToExcel()
    gateway.shutdown()

main()