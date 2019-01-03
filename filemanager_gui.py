#!/usr/bin/env python

from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter import filedialog


def folder_finder_gui():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = filedialog.askdirectory() # show an "Open" dialog box and return the path to the selected file
    return filename

if __name__ == '__main__':
    print(folder_finder_gui())