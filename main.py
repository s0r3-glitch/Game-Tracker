import core.configfile as config
from core.startingchecks import checks
from core.localcommands import clear, pause, title
import os
import art
from colorama import Fore, init
import pymongo
import requests
import json

# initalized colorama
init()

# Prints the s0r3-glitch name
print(Fore.CYAN + art.text2art('s0r3-glitch', font='block', chr_ignore=True))

#checks to see if the config file exists
checks()
    

# Getting the steam web API info from the config file
WebAPIKey = config.ReadConfig('Steam', 'webapikey')
print(WebAPIKey)

SteamID = config.ReadConfig('Steam', 'steamid')
print(SteamID)

# Getting the DB ip info from the config file
ClientAdderess = config.ReadConfig('DBinfo', 'clientaddress')
print(ClientAdderess)

# Getting the DB port info from the config file
ClientPort = config.ReadConfig('DBinfo', 'clientport')
print(ClientPort)

DBaddress = f'mongodb://{ClientAdderess}:{ClientPort}/'

# Gets the DB name from the config
DBname = config.ReadConfig('DBinfo', 'dbname')
print(DBname)

# Connecting to the MongoDO and specifying the DB we are going to use
print('beep')
myclient = pymongo.MongoClient(DBaddress)
mydb = myclient[DBname]
mycol = mydb['Games']
print(mydb.list_collection_names())
steamresponse = requests.get(f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={WebAPIKey}&steamid={SteamID}&include_appinfo=1")
y = json.loads(steamresponse.text)
print(y["response"]["game_count"])
for i in range(y["response"]["game_count"]):
    query = { "appid": y['response']['games'][i]['appid'] }
    mydoc = mycol.find(query)
    for x in mydoc:
        print(x)
    if mydb.list_collection_names() == []:
        entrie = {"name": y['response']['games'][i]['name'], "platform": "Steam", "Type": "Digital", "Location": "Digital", "img_icon": y['response']['games'][i]['img_icon_url'], "img_logo": y['response']['games'][i]['img_logo_url'], "appid": y['response']['games'][i]['appid']} 
        x = mycol.insert_one(entrie)
    elif mydoc == '':
        entrie = {"name": y['response']['games'][i]['name'], "platform": "Steam", "Type": "Digital", "Location": "Digital", "img_icon": y['response']['games'][i]['img_icon_url'], "img_logo": y['response']['games'][i]['img_logo_url'], "appid": y['response']['games'][i]['appid']} 
        x = mycol.insert_one(entrie)
    else:
        print('Game match sorry')