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


### 3 choix: liste/add/del
# si add:
# on ajoute le projet -> créer le fichier (si fichier déjà existant alors on le met dedans)
# si remove
# on del le projet

#list on montre la liste




num = 0

def list__():
    none = ""
    print(bg+"Write '-h' if current dir."+r)
    parent_dir = str(input("Parent dir: "))
    path = os.path.join(parent_dir)
    if parent_dir == "-h":
        print(os.listdir())
    else:
        print(os.listdir(path))
    menu()
    


def remove():
    print("REMOVE METHOD")

    print("Folder -F or file -f ?")
    way = str(input("> "))

    if way == "-F":
        parent_dir = str(input("Parent dir: "))
        path = os.path.join(parent_dir)
        isExist = os.path.exists(path)
        if isExist == False:
            print(br + "/!\ This folder/dir doesn't exist.")
            menu()
        else:
            shutil.rmtree(path)
            s = str(input(""))



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
            menu()
        
        else:
            print("Which files you want to delete ?")
            print(os.listdir(path))
            filedel = str(input("filename.ext > "))
            os.remove(path + "\\" + filedel)
            #s = str(input(""))
    
    print("File(s) / Folder(s) successfully deleted.")
    menu()






def add():
    print("ADD METHOD")
    directory = str(input("Folder name:"))
    if directory == None:
        print(br+"/!\\ You have to set a folder name." + r)
 
    parent_dir = str(input("Parent dir: "))
    
    path = os.path.join(parent_dir, directory)
    isExist = os.path.exists(path)

    if isExist == False:
        os.mkdir(path)
        print("Folder created perfectly.")
        print("What files do you want to write in ?")
        print("write 'DONE' or '-d' if done, 'NULL' or '-n' if nothing.")
    
    make = True
    while make:
        fn = str(input("File name > "))

        if fn == "NULL" or fn == "-n":
            break
        
        if fn == "DONE" or fn == "-d":
            print("ok?")
            break

        ext = str(input("Extension > "))

        final = fn + '.' + ext
        complete = os.path.join(path, final)
        file1 = open(complete, "w")
        file1.write("")
        file1.close()

        print(f"Successfully created at {path} !")



        #with open(f'{s_path}+{fn}.{ext}', 'a') as f:
        #    f.write(f"")

        
    


        
        
       

    #path[str(path)]["dir"] = path
    #path[str(path)] = {}
#
    #with open("data.json", 'w') as f:
    #    json.dump(path,f)

    
def menu():
    print(bg+"FILE-PROJECT MANAGER"+r)
    list_ = True
    while list_:
        print("List")
        print("Add")
        print("Remove")
        met = str(input("> "))
        if met == "list" or met == "List":
            list__() 
            list_ = False
        elif met == "add" or met == "Add":
            add()
            list_ = False
        elif met == "remove" or met == "Remove":
            remove()
            list_ = False

menu()