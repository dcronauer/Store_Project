#this will provide the gui framework for the store.py file
import tkinter
from tkinter import ttk
from tkinter import messagebox
from store import *



def main():
    create_window = Store_Gui()

    #set up main loop for gui
    tkinter.mainloop()

class Store_Gui:
    list_stores = []
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.instance = tkinter.StringVar()
        self.store_id = tkinter.IntVar()
        self.store_address = tkinter.StringVar()
        self.create_objects()
    
    def create_objects(self):
        #create frames
        self.store_creation_frame = tkinter.Frame(self.main_window)
        self.inventory_management_frame = tkinter.Frame(self.main_window)
        self.register_frame = tkinter.Frame(self.main_window)

        #create widgets store_creation_frame
        self.store_initialize_label_instance = ttk.Label(self.store_creation_frame,text="Enter instance name for new store: ")
        self.store_initialize_entry_instance = ttk.Entry(self.store_creation_frame,textvariable=self.instance, width = 15)
        self.store_initialize_label_id = ttk.Label(self.store_creation_frame,text="Enter id for new store: ")
        self.store_initialize_entry_id = ttk.Entry(self.store_creation_frame,textvariable=self.store_id, width = 15)
        self.store_initialize_label_city = ttk.Label(self.store_creation_frame,text="Enter city location of store being created: ")
        self.store_initialize_entry_id = ttk.Entry(self.store_creation_frame,textvariable=self.store_address, width = 15)

        self.store_inialize_button = ttk.Button(self.store_creation_frame,text="Create new store",command=self.create_store)

        #pack widgets
        self.store_initialize_label_instance.pack(side="left")
        self.store_initialize_entry_instance.pack(side="left")
        self.store_initialize_label_id.pack(side="left")
        self.store_initialize_entry_id.pack(side="left")
        self.store_initialize_label_city.pack(side="left")
        self.store_initialize_entry_city.pack(side="left")
        self.store_initialize_button.pack(side="left")





    def create_store(self):
        create = self.instance.get()
        create = store.Store(self.store_id.get(),self.store_address.get())

        string = print(store.Store.store_dict_get())
        tkinter.messagebox.showinfo('Entry Complete',f'Here is the updated store listing {string}')

        self.instance.set('')
        self.store_id_set('')
        self.store_addess_set('')





if __name__ == "__main__":
    main()