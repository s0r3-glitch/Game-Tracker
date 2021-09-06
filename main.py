import core.configfile as config
from core.startingchecks import checks
from core.localcommands import clear, pause, title
import os
import art
from colorama import Fore, init
import pymongo
import requests

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
# print('beep')
# myclient = pymongo.MongoClient(DBaddress)
# mydb = myclient[DBname]
# mycol = mydb['Games']
# print(mydb.list_collection_names())

# mydict = { "name": "John", "address": "Highway 37" }
# x = mycolSteam.insert_one(mydict)
# print('boop')
# x = mycolSteam.find_one()
# print(x)

steamresponse = requests.get(f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={WebAPIKey}&steamid={SteamID}&include_appinfo=1")
print(steamresponse.text)
print(type(steamresponse.text))