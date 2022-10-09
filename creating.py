import projectsmanager

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

def add():
    print("CREATE METHOD")
    directory = str(input("Folder name (enter is just file making):"))
    #if directory == None:
    #    print(br+"/!\\ You have to set a folder name." + r)
 
    parent_dir = str(input("Parent dir: "))
    
    path = os.path.join(parent_dir, directory)
    isExist = os.path.exists(path)

    if isExist == False:
        os.mkdir(path)
        print(fg + "Folder created perfectly." + fr)
        print("What files do you want to write in ?")
        print("write 'DONE' or '-d' if done, 'NULL' or '-n' if nothing.")
    
    make = True
    while make:
        fn = str(input("File name > "))

        if fn == "NULL" or fn == "-n":
            break
        
        if fn == "DONE" or fn == "-d":
            break

        ext = str(input("Extension > "))

        final = fn + '.' + ext
        complete = os.path.join(path, final)
        file1 = open(complete, "w")
        file1.write("")
        file1.close()

        print(f"{fg} Successfully created at {path} !" + fr)
    projectsmanager.menu()
projectsmanager.menu()

