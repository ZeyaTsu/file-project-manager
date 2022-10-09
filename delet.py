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

def remove():
    print("DELETE METHOD")

    print("Folder -F or file -f ?")
    way = str(input("> "))

    if way == "-F":
        parent_dir = str(input("Parent dir: "))
        path = os.path.join(parent_dir)
        isExist = os.path.exists(path)
        if isExist == False:
            print(br + "/!\ This folder/dir doesn't exist.")
            projectsmanager.menu()
        else:
            shutil.rmtree(path)
            #s = str(input(""))
            time.sleep(2)



    if way == '-f':


        directory = str(input("Folder name:"))
        if directory == "None" or directory == "-n":
            parent_dir = str(input("Parent dir: "))
            
            path = os.path.join(parent_dir)
            isExist = os.path.exists(path)
            
            
    
        else:


            parent_dir = str(input("Parent dir: "))
            
            
            path = os.path.join(parent_dir, directory)
            isExist = os.path.exists(path)

        if isExist == False:
            print(br + "/!\ This folder/dir doesn't exist.")
            projectsmanager.menu()
        
        else:
            print(fg + "Which files you want to delete ?" + fr)
            print(os.listdir(path))
            filedel = str(input("filename.ext > "))
            if filedel == "-n" or filedel == "None":
                projectsmanager.menu()
            else:
                os.remove(path + "\\" + filedel)
            #s = str(input(""))
    
    print(fg + "File(s) / Folder(s) successfully deleted." + fr)
    projectsmanager.menu()