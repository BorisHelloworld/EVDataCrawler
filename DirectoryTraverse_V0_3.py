import os, os.path

def func_DirWalkThrough(dir_name):
    list_webaddr = []
    for root, _, files in os.walk(dir_name):
        for f in files:
             name_txt = f.split('.')
             #print name_txt[0]
             fullpath = "http://www.chargecar.org/data/" + name_txt[0]
             list_webaddr.append(fullpath)

    return list_webaddr

                    
                 
