import requests
import threading
from colorama import Fore, Back, Style


print(
        Fore.YELLOW +
         """
   ____                                    
|  _ \ _   _ _ __ ___  _ ____  _____ ___ 
| | | | | | | '_ ` _ \| '_ \ \/ / __/ __|
| |_| | |_| | | | | | | |_) >  <\__ \__ \
|____/ \__,_|_| |_| |_| .__/_/\_\___/___/
                      |_|  
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
