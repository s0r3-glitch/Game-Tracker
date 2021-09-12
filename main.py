import core.configfile as config
from core.startingchecks import checks
from core.localcommands import clear, pause, title
import core.dbinteraction as dbintra
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

# Makes sure the config file is present
checks()

# Gets the db info from the config
DBaddress, DBname, ClientIP = config.dbconfig()



def main():
    loop = True
    clear()
    while loop is True:
        print(Fore.CYAN + art.text2art('Game-Tracker', font='block', chr_ignore=True))
        choice = int(input('What would you like to do today?\n1. Update your Steam Libreary\n2. Manually add a game\n3. Exit\n'))
        if choice == 1:
            Webapi, SteamID = config.steamconfig()
            dbintra.Steamautoadd(DBaddress, DBname, Webapi, SteamID)
            clear()
        elif choice == 2:
            dbintra.ManualAdd(DBaddress,DBaddress)
            clear()
        elif choice == 3:
            exit(0)

main()
