#!/usr/bin/env python

import os
from filemanager_gui import folder_finder_gui
from time import sleep

# This is the module to traverse through all the files present in the given sub directory

# This function is to convert from bytes to MB, GB, etc
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

# This function returns a list of all the files with matching extension in the directory 
# Extension can either be a list or a string

def list_all_files(directory,extension):
    items = []
    sizes = []
    if type(extension) is str:
        for root, dirs, files in os.walk(directory):  
            for filename in files:
                if extension in filename:
                    filepath = os.path.join(root, filename)
                    filesize = convert_bytes(os.stat(filepath).st_size)

                    items.append(filepath)
                    sizes.append(filesize)
    
    elif type(extension) is list:
        for root, dirs, files in os.walk(directory):  
            for filename in files:
                for i in extension:
                    if i in filename:
                        filepath = os.path.join(root, filename)
                        filesize = convert_bytes(os.stat(filepath).st_size)

                        items.append(filepath)
                        sizes.append(filesize)
    
    return {'items' : items, 'sizes' : sizes }

# This function lists all the folders in the directory with said extension
def list_files_in_folder(directory,extension):
    listOfFiles = os.listdir(directory)
    items = []
    sizes = []

    if type(extension) is str:
        for i in listOfFiles: 
            if extension in i:
                filepath = os.path.join(directory,i)
                filesize = convert_bytes(os.stat(filepath).st_size)

                items.append(filepath)
                sizes.append(filesize)
    
    elif type(extension) is list:
        for filename in listOfFiles:
            for i in extension:
                if i in filename:
                    filepath = os.path.join(directory,i)
                    filesize = convert_bytes(os.stat(filepath).st_size)

                    items.append(filepath)
                    sizes.append(filesize)

    return {'items' : items, 'sizes' : sizes }

# Mode 
# 0 ---> List all files in all sub directories too
# 1 ---> List all files in current directory only
def main(ext, mode = 0):
    path = folder_finder_gui()
    
    stuff = {}

    if mode:
        stuff = list_files_in_folder(path,ext)
    else:
        stuff = list_all_files(path,ext)

    return stuff

if __name__ == '__main__':
    print(main('.txt',0))
    sleep(5)
    # a = list_all_files('d:\\',['.mp3','.py'])
    # print(a['items'])
    # print(a['sizes'])
    # b = list_files_in_folder('d:\\','.py')
    # print(b["items"])
    # print(b["sizes"])
