#this will provide the gui framework for the store.py file

import tkinter
from tkinter import ttk

class Store_Gui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.create_objects()
    
    def create_objects