import time
import re
from bs4 import BeautifulSoup as bs
import requests as req
import openpyxl
import random
from user_collections.users import arr
from user_collections.CPMy import arr1

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
"Mozilla/5.0 (Windows; U; Windows NT 10.0;) AppleWebKit/535.25 (KHTML, like Gecko) Chrome/55.0.2176.177 Safari/534.5 Edge/9.78105",
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_5; like Mac OS X) AppleWebKit/600.22 (KHTML, like Gecko) Chrome/48.0.1537.263 Mobile Safari/600.2",
"Mozilla/5.0 (Linux; U; Linux x86_64; en-US) Gecko/20100101 Firefox/54.7"
]

proxies = [

]

testUser = [

]

toSave = [
    
]

sesh = req.Session()
baseURL = "https://google.com/search?q="

def saveToExcel():
    wb = openpyxl.Workbook()
    ws = wb.active
    for tuples in toSave:
        ws.append([tuples[0], tuples[1], tuples[2]])
    wb.save("trademark_usage.xlsx")

def executeSearch(fname, lname, abbr, cert):
    headers = {
        "User-Agent": random.choice(userAgents)
    }
    proxies = {
        "http": "http://104.21.31.189",
        "https": "https://104.21.31.189"
    }
    try: 
        response2 = req.get(f'{baseURL}{fname}+{lname}+{cert}', proxies=proxies, headers=headers)
        print(f"{baseURL}{fname}+{lname}+{cert}")
    except Exception as e:
        print(e)
        return False
    print(response2.status_code)
    response2 = str(bs((response2.content), "html.parser"))
    match = re.search((fr"(?i)(?:{fname}\s*?.{{0,11}}?\s*?{lname}[\s\S]{{0,15}}?{abbr})"), response2)
    if (match):
        toSave.append([fname, lname, match.group()])
        return True
    else:
        return False

def main():
    count=0
    for identity in arr1:
        if (count <= 125):
            count+= 1
            print(identity)
            returner = executeSearch(identity[0], identity[1], "CPM", "Certified Property Manager")
          #  if not returner:
         #       returner = executeSearch(identity[0], identity[1], "ARM", "Accredited Residential Manager")
          #  if not returner:
          #      returner = executeSearch(identity[0], identity[1], "ACoM", "Accredited Commercial Manager")
            print(count, returner)
        else:
            saveToExcel()
            break
            


main()


#        with open(file_path, "w") as file:
         #E   file.write(response2)
         
'''
         try:
        with open(fname+cert, "w") as file:
            file.write(response2)
    except:
        print("ASD")
        https://requests.readthedocs.io/en/latest/user/advanced/
        https://stackoverflow.com/questions/10606133/sending-user-agent-using-requests-library-in-python
        https://dashboard.scraperapi.com/billing
        https://requests.readthedocs.io/en/latest/user/advanced/
        import requests
            headers = {
        "User-Agent": random.choice(userAgents)
    }
    proxies = {
        "http": "http://104.21.31.189",
        "https": "https://104.21.31.189"
    }
from requests_ip_rotator import ApiGateway, EXTRA_REGIONS

gateway = ApiGateway("https://www.transfermarkt.es")
gateway.start()

session = requests.Session()
session.mount("https://www.transfermarkt.es", gateway)

response = session.get("https://www.transfermarkt.es/jadon-sancho/profil/spieler/your_id")
print(response.status_code)

# Only run this line if you are no longer going to run the script, as it takes longer to boot up again next time.
gateway.shutdown() 
https://github.com/Ge0rg3/requests-ip-rotator
https://free-proxy-list.net/

        '''