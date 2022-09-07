import json
import requests
from colorama import Back, Fore, Style
import time

time.sleep(0.10)


banner = '''



███████████████████████████████████████████████████████
█─▄▄─█─▄▄▄▄█▄─▄█▄─▀█▄─▄█─▄─▄─█▀▀▀▀▀██▄─█─▄█▄─▄▄▀█▄─▄▄▀█
█─██─█▄▄▄▄─██─███─█▄▀─████─███████████─▄▀███─▄─▄██─██─█
▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▀▀▀▀▀▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀


$==> Title : OSINT-Krd
$==> Coder : LulzKrd Team Krd-Pentester
$==> Version : Latest 
$==> Programming Language : Python
$==> Github : github.com/krdsploit
$==> YTB : Krd Pentester


                                    '''

time.sleep(0.10)


print(Fore.YELLOW + banner)



img_url = input("Enter The Image Url : ")


url = "https://api.apilayer.com/violence_detection/url?url="+img_url


payload = {}
headers= {
  "apikey": "iQHJExGt6zflQUsTrtDaSnwihvOI4Pe6"
}

response = requests.request("GET", url, headers=headers, data = payload)

responses = response.text
results = json.loads(responses)

print("Violence " + results['description'])
print("Value " + (str(results['value'])))