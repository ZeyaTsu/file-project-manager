import projectsmanager

import time
import os 
import json
import shutil
import colorama
from colorama import Fore, Back, Style
from colorama import init
init()
bg = Back.BLUE
r = Back.BLACK
br = Back.RED
fg = Fore.GREEN
fr = Fore.WHITE

def list__():
    none = ""
    print(bg+"Write '-h' if current dir."+r)
    parent_dir = str(input("Parent dir: "))
    path = os.path.join(parent_dir)
    if parent_dir == "-h":
        print(os.listdir())
    elif parent_dir == "showcd":
        print(fg + os.getcwd() + fr)
    
    else:
        print(os.listdir(path))
    projectsmanager.menu()
    

   
    