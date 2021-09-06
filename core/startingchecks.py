import os
from core.configfile import CreateConfig, ReadConfig
from core.localcommands import clear, pause
from colorama import Fore, Back

# General check function used by the main program. This is the only function that should be called by any other program
def checks():
    ConfigPresents()
    ConfigRead()
    ConfigWebAPICheck()

# Checks to make sure the config file exists if not it generates it
def ConfigPresents():
    if os.path.isfile('./config.ini') == False:
        print(Back.RED + 'Error 0')
        print(Fore.YELLOW + 'Config file not found...\nGenerating config file...\n')
        try:
            CreateConfig()
            print(Fore.GREEN + 'Please check the README to properly set up the config file')
        except Exception:
            print(Back.RED + 'Error 2')
        pause()
        exit(0)
    else:
        print('Config file found...')

# Checks to see if the program can read the config file
def ConfigRead():
    try:
        temp = open('./config.ini', 'r')
        temp.close()
    except Exception:
        print(Back.RED + 'Error 3')
        pause()
        exit(0)

# Checks to see if the Web API is present
def ConfigWebAPICheck():
    if ReadConfig('Steam', 'webapikey') == 'N/A' or '':
        print(Back.RED + 'Error 1')
        pause()
        exit(0)