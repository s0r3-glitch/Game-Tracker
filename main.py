import core.configfile as config
from core.startingchecks import checks
from core.localcommands import clear, pause, title
from core.steamwebapi import Steamautoadd
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

def ManualAdd():
    myclient = pymongo.MongoClient(DBaddress)
    mydb = myclient[DBname]
    mycol = mydb['Games']
    loop = True
    while loop is True:
        clear()
        name = str(input('Name of the game:'))
        name = name.title()
        platform = str(input('Platform the game is on:'))
        platform = platform.title()
        type = str(input('Is the game physical or digital:'))
        type = type.title()
        if type == 'Digital':
            location = 'Digital'
        else:
            location = str(input('Where is the game now:'))
        entrie = {"name": name, "platform": platform, "Type": type, "Location": location}
        x = mycol.insert_one(entrie)
        temp = str(input('Would you like to add more game (yes or no):'))
        temp = temp.title()
        if temp == 'No':
            loop = False

def main():
    loop = True
    clear()
    while loop is True:
        print(Fore.CYAN + art.text2art('Game-Tracker', font='block', chr_ignore=True))
        choice = int(input('What would you like to do today?\n1. Update your Steam Libreary\n2. Manually add a game\n3. Exit\n'))
        if choice == 1:
            Steamautoadd()
            clear()
        elif choice == 2:
            ManualAdd()
            clear()
        elif choice == 3:
            exit(0)

main()
