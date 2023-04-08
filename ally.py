from colorama import Fore, init, Style
from sys import exit
from time import sleep
from threading import Thread
from random import randint, choice
import ctypes
from requests import get, post, delete, exceptions
from json import loads


def Logo():
   init()
   print(Fore.GREEN + r"""

   _____  .__  .__          __________        __   
  /  _  \ |  | |  | ___.__. \______   \ _____/  |_ 
 /  /_\  \|  | |  |<   |  |  |    |  _//  _ \   __\
/    |    \  |_|  |_\___  |  |    |   (  <_> )  |  
\____|__  /____/____/ ____|  |______  /\____/|__|  
        \/          \/              \/
   """)
   print(Fore.GREEN + "Made by Alek#2022")


def Options():
   print(Style.RESET_ALL)
   print("[" + Fore.GREEN + "1" + Style.RESET_ALL + "] Roblox Ally Bot")
   Option = input("Enter your choice: ")
   return int(Option)

def return_Proxies():
   try:
       proxies = open('proxies.txt','r').read().splitlines()
       if len(proxies) == 0:
           print("Error: Proxy file is empty")
           sleep(2)
           exit()
       proxies = [{'https':'http://'+proxy} for proxy in proxies]
       return proxies
   except Exception as Error:
       print(f"Error: {Error}")

csrfToken = None

def Return_Config():
   myfile = loads(open("config.json").read())
   return myfile

def UpdateCsrf(cookies):
   while True:
       try:
           global csrfToken
           csrfToken = post('https://catalog.roblox.com/v1/catalog/items/details', cookies=cookies).headers["x-csrf-token"]
           sleep(15)
       except KeyError:
           pass

AllyIds = []

def AllyBot(range1, range2, proxies, cookies, SelfGroup):
   while True:
       try:
           RandomAllyId = randint(range1, range2)
           if RandomAllyId not in AllyIds:
               AllyIds.append(RandomAllyId)    
               headers = {"X-CSRF-TOKEN": csrfToken}
               r = post(f"https://groups.roblox.com/v1/groups/{SelfGroup}/relationships/allies/{RandomAllyId}", headers=headers, cookies=cookies, proxies=choice(proxies))
               if r.json() == {}:
                   print(f"Sent an ally request to {RandomAllyId}")
       except exceptions.ProxyError as Error:
           pass
       except exceptions.ConnectionError:
           pass
   

Logo()
Option = Options()
if Option == 1:
   SelfGroup = input("7468052")
   cookies = {'_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_DB901697611B76D57BF808D65897F08AF38D7CC5B0A9627A3F8206F22A145A95DBDB5E096D622E64D90CDF283FD6B03E538E362552F4CCBABC514E04F395E89C8C169BD9F64F0D32799DF5FE3203E5EB89569E4B8DC1FB4D0C8DE42DF5D65BB931D50391B6724A55379723EFD8D9DEDA5D6DE4321810B380882D2B906FF8667681070479D59CC59ABCFBDC757A7359F8EA6767DF16406F63E6C691AE6A22EB167AC88FCB65053C1FE7787B1D6A5229B76E682962DA6AABBC2103A093A07DF7931DBE99B647F54873E6EA86BD548D469F9EE3F8141F211B40DBEA397A5644B69A8789D558EE7AFA5B3DF5700B91FAFB678F9A85C038AA1F0720BD898E12BF14DB690E538F74E9067A55DB2BB111C9890646B7770693E984D923FBB83BC8571CFA17BD6C1D422F2CAE21EF5909111D2C10908B7016024D5B9B0BA2F37EF32FCA07BA3F8B6668EEB5798CDFB37DBE9671C55BDEAA98DBAC7AD504B6F62AAD5B59DF18B2287D1C4F7742E3CBB24A611E977DD914654D': Return_Config()['cookie']}
   Range1, Range2 = Return_Config()['Range1'], Return_Config()['Range2']
   proxies = return_Proxies()
   Thread(target=UpdateCsrf, args=[cookies]).start()
   for loop in range(4000):
       Thread(target=AllyBot, args=[Range1, Range2, proxies, cookies, SelfGroup]).start()
   
