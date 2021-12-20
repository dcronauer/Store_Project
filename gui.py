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
        self.item_name = tkinter.StringVar()
        self.item_price = tkinter.IntVar()
        self.item_count = tkinter.IntVar()
        self.list_box_stores = tkinter.StringVar(value=Store_Gui.list_stores)
        
        self.create_objects()
    def __str__(self):
        return f'{Store_Gui.list_stores}'
        
    
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
        self.store_initialize_entry_city = ttk.Entry(self.store_creation_frame,textvariable=self.store_address, width = 15)

        self.store_initialize_button = ttk.Button(self.store_creation_frame,text="Create new store",command=self.create_store)

        #pack widgets store_creation_frame
        self.store_initialize_label_instance.pack(side="left")
        self.store_initialize_entry_instance.pack(side="left")
        self.store_initialize_label_id.pack(side="left")
        self.store_initialize_entry_id.pack(side="left")
        self.store_initialize_label_city.pack(side="left")
        self.store_initialize_entry_city.pack(side="left")
        self.store_initialize_button.pack(side="left")

        #pack store_creation_frame frame
        self.store_creation_frame.pack()

        #create widgets inventory_management_frame
        self.display_stores_listbox = ttk.Combobox(self.inventory_management_frame,value=Store_Gui.list_stores,postcommand = self.update_store_list)
        self.inventory_label_item = ttk.Label(self.inventory_management_frame,text="Item Name")
        self.inventory_entry_item = ttk.Entry(self.inventory_management_frame, textvariable=self.item_name, width=15)
        self.inventory_label_price = ttk.Label(self.inventory_management_frame,text="Item Price")
        self.inventory_entry_price = ttk.Entry(self.inventory_management_frame,textvariable=self.item_price, width=15)
        self.inventory_label_count = ttk.Label(self.inventory_management_frame,text="Item Count")
        self.inventory_entry_count = ttk.Entry(self.inventory_management_frame,textvariable=self.item_count, width=15)
        self.inventory_button = ttk.Button(self.inventory_management_frame,text="Add inventory item to store",command=self.add_item)

        #pack widgets iventory management frame
        self.display_stores_listbox.pack(side="left")
        self.inventory_label_item.pack(side='left')
        self.inventory_entry_item.pack(side="left") 
        self.inventory_label_price.pack(side="left") 
        self.inventory_entry_price.pack(side="left") 
        self.inventory_label_count.pack(side="left") 
        self.inventory_entry_count.pack(side="left")
        self.inventory_button.pack(side="left")

        #pack inventory management frame
        self.inventory_management_frame.pack()

    def create_store(self):
        create = self.instance.get()
        
        create = Inventory(self.store_id.get(),self.store_address.get())
        Store_Gui.list_stores.append(create)
        string = Store.store_dict_get()
        tkinter.messagebox.showinfo('Entry Complete',f'Here is the updated store listing {string}')
        item = Store_Gui.list_stores
        
        self.instance.set('')
        self.store_id.set('')
        self.store_address.set('')
    def update_store_list(self):
        
        self.display_stores_listbox.set(Store_Gui.list_stores)
    def add_item(self):
        item = self.inventory_entry_item.get()
        price = self.inventory_entry_price.get()
        count = self.inventory_entry_count.get()
        
        
        new_item = Store_Gui.list_stores[0].new_item(item,price,count)


        print(Store_Gui.list_stores[0].print_inventory_items())


        
if __name__ == "__main__":
    main()