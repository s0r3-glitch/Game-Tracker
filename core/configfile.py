'''
This file contains functions that interact with the config file
'''

import configparser

config = configparser.ConfigParser()

# Used to read data from the config file
def ReadConfig(section, datatype):
    config.read('config.ini')
    # print(section)
    # print(section in config)
    # print(datatype)
    # print(config.sections())
    # print(config[section][datatype])
    return config[section][datatype]

# Used to create the config file
def CreateConfig():
    config['Steam'] = {'WebAPIkey': '',
                        'SteamID': ''}
    config['DBinfo'] = {'ClientAddress': '',
                        'ClientPort': '27017',
                        'DBName': ''}
    config['Manualaddinfo'] = {'Data': 'name, platform, type, location'}
    config['Xbox'] = {'ApplicationID': '',
                      'SecretID': '',
                      'XboxUID': ''}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
        
# Used for loading DB config info
def dbconfig():
  # Getting the DB ip info from the config file
  ClientAdderess = config.ReadConfig('DBinfo', 'clientaddress')
  print(ClientAdderess)

  # Getting the DB port info from the config file
  ClientPort = config.ReadConfig('DBinfo', 'clientport')
  print(ClientPort)
  
  # builds the DB address
  DBaddress = f'mongodb://{ClientAdderess}:{ClientPort}/'
  
  # Gets the DB name from the config
  DBname = config.ReadConfig('DBinfo', 'dbname')
  print(DBname)
  
  return(DBaddress, DBname, ClientAddress)
  
# Loads the steam config data
def steamconfig():
  # Getting the steam web API info from the config file
  WebAPIKey = config.ReadConfig('Steam', 'webapikey')
  print(WebAPIKey)
  
  SteamID = config.ReadConfig('Steam', 'steamid')
  print(SteamID)
  
  return(WebAPIkey, SteamID)
  
def manualconfig():
  data = list(config.ReadConfig('Manualaddinfo', 'Data'))
  return data
  
def xboxconfig():
  AppID = config.ReadConfig('Xbox', 'ApplicationID')
  SecID = config.ReadConfig('Xbox', 'SecretID')
  XUID = config.ReadConfig('Xbox', 'XboxUID')
  return AppID, SecID, XUID