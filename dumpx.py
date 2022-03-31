import requests
import threading
from colorama import Fore, Back, Style


print(
        Fore.YELLOW +
         """
     888
     888
     888
 .d88888 888  888 88888b.d88b.  88888b.  888  888
d88" 888 888  888 888 "888 "88b 888 "88b `Y8bd8P'
888  888 888  888 888  888  888 888  888   X88K
Y88b 888 Y88b 888 888  888  888 888 d88P .d8""8b.
 "Y88888  "Y88888 888  888  888 88888P"  888  888
                                888
                                888
                                888
                                          [ twitter.com/r00t_nasser ]
                                          [ Snapchat : aaa.saq ]
        """ + Fore.RESET)

print()
print()
file = open('url.txt','r')
payloads = open('payloads.txt','r')
def Send_req(url,payload):
    #while url[-1] != '=':
     #   url = url[:-1]
    url = url.replace("=",f"={payload}")

    try:

        res = requests.get(url)
        if payload in res.text:
           print(Fore.GREEN +'XSS Found   -->','   ' , f"{url}" + Fore.RESET)


    except Exception as e:
        pass
file = file.readlines()
for payload in payloads:
    for url in file:
        url = url.strip('\n')
        payload = payload.strip('\n')
        threading.Thread(target=Send_req,args=(url,payload,)).start()
