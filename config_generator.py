import configparser
config = configparser.ConfigParser()
config['Steam'] = {'WebAPIkey': '',
                     'AccessToken': '',
                     'SteamID': ''}
config['DBinfo'] = {'ClientAddress': '',
                    'DBName': '',
                    'CollectionName': ''}
with open('config.ini', 'w') as configfile:
  config.write(configfile)