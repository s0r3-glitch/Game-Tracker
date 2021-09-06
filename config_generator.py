import configparser
config = configparser.ConfigParser()
config['Steam'] = {'WebAPIkey': '',
                     'SteamID': ''}
config['DBinfo'] = {'ClientAddress': '',
                    'ClientPort': '27017',
                    'DBName': '',
                    'CollectionName': ''}
with open('config.ini', 'w') as configfile:
  config.write(configfile)