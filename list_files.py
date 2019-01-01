#!/usr/bin/env python

import os

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
        for root, dirs, files in os.walk("."):  
            for filename in files:
                for i in extension:
                    if i in filename:
                        filepath = os.path.join(root, filename)
                        filesize = convert_bytes(os.stat(filepath).st_size)

                        items.append(filepath)
                        sizes.append(filesize)
    
    return {'items' : items, 'sizes' : sizes }


if __name__ == '__main__':
    a = list_all_files('d:\\','.py')    # Printing all files in D: with the .py extension
    print(a['items'])
    print(a['sizes'])
