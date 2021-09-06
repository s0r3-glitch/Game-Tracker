import os
from configfile import CreateConfig
from colorama import Fore

def startchecks():
    configpresents()

def configpresents():
    if os.path.isfile('./config.ini') == False:
        print(Fore.RED + 'Config file not found...\nGenerating config file...\n')
        CreateConfig()
        print(Fore.YELLOW + 'Please check the README to properly set up the config file')
        print(input('Press any key to continue...'))
        exit(0)
