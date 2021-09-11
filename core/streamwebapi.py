import pymongo
import requests
from colorama import Fore
import json

# Connecting to the MongoDO and specifying the DB we are going to use
def Steamautoadd():
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
