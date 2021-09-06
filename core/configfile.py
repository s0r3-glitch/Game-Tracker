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
                        'AccessToken': 'N/A',
                        'SteamID': ''}
    config['DBinfo'] = {'ClientAddress': '',
                        'DBName': 'mongodb://',
                        'CollectionName': 'N/A'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)