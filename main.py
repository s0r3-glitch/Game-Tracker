import core.configfile as config
from core.localcommands import clear, pause, title
import os
import art
from colorama import Fore, init

# initalized colorama
init()

# Prints the s0r3-glitch name
print(Fore.CYAN + art.text2art('s0r3-glitch', font='block', chr_ignore=True))

#checks to see if the config file exists

    

# Getting the steam web API info from the config file
WebAPIKey = config.ReadConfig('Steam', 'webapikey')
print(WebAPIKey)
AccessToken = config.ReadConfig('Steam', 'accesstoken')
print(AccessToken)
SteamID = config.ReadConfig('Steam', 'steamid')
print(SteamID)

# Getting the DB info from the config file
ClientAdderess = config.ReadConfig('DBinfo', 'clientaddress')
print(ClientAdderess)
DBname = config.ReadConfig('DBinfo', 'dbname')
print(DBname)