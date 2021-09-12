'''
This file contains any functions that directly interacts with the database
'''
import pymongo
import requests
from colorama import Fore
import json

# Manually adds games to the db
def ManualAdd(DBaddress, DBname, data):
    local data
    entrie = {}
    myclient = pymongo.MongoClient(DBaddress)
    mydb = myclient[DBname]
    mycol = mydb['Games']
    loop = True
    while loop is True:
      clear
      for i in len(data):
        entrie[data[i]] = str(input(f'Game {data[i]}: '))
      x = mycol.insert_one(entrie)
      temp = str(input('Would you like to add more game (yes or no):'))
      temp = temp.title()
      if temp == 'No':
          loop = False
        
      
    
    '''
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
            '''

# Connecting to the MongoDO and specifying the DB we are going to use
def Steamautoadd(DBaddress, DBname, WebAPIKey, SteamID):
    #print('beep')
    myclient = pymongo.MongoClient(DBaddress)
    mydb = myclient[DBname]
    mycol = mydb['Games']
    #print(mydb.list_collection_names())
    steamresponse = requests.get(f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={WebAPIKey}&steamid={SteamID}&include_appinfo=1")
    y = json.loads(steamresponse.text)
    #print(y["response"]["game_count"])
    newlyadded = 0
    skipped = 0
    for i in range(y["response"]["game_count"]):
        query = { "appid": y['response']['games'][i]['appid'] }
        mydoc = mycol.find(query)
        if not mydb.list_collection_names():
            #print('1')
            entrie = {"name": y['response']['games'][i]['name'], "platform": "Steam", "Type": "Digital", "Location": "Digital", "img_icon": y['response']['games'][i]['img_icon_url'], "img_logo": y['response']['games'][i]['img_logo_url'], "appid": y['response']['games'][i]['appid']} 
            x = mycol.insert_one(entrie)
            newlyadded += 1 
        elif mydoc.count() == 0:
            #print(2)
            entrie = {"name": y['response']['games'][i]['name'], "platform": "Steam", "Type": "Digital", "Location": "Digital", "img_icon": y['response']['games'][i]['img_icon_url'], "img_logo": y['response']['games'][i]['img_logo_url'], "appid": y['response']['games'][i]['appid']} 
            x = mycol.insert_one(entrie)
            newlyadded =+ 1
        else:
            #print('Game exists in DB')
            skipped += 1
    print(Fore.GREEN + f'Steam library update complete:\nNewly added game: {newlyadded}\nGames skipped: {skipped}')
    pause()
