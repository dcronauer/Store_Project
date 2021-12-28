#this will provide the gui framework for the store.py file
import tkinter
from tkinter import ttk
from tkinter import simpledialog
from store import *
import dill


def main(): 
    create_window = Store_Gui()   
    #set up main loop for gui
    tkinter.mainloop()
class Store_Gui:
    list_stores = [] #collection of store instances created
    id_stores = [] #list of store ids
    list_register = []
    id_register = []

    
    #key is register id and value is register instance
    registerid_instance_dict = dict()  
    #key is store_id value is list of register ids
    register_dict = dict()  
    
    
    def __init__(self):
        self.main_window = tkinter.Tk()
        dill.load_session('dump.pkl')
        self.id_store_get()
        
        self.instance = tkinter.StringVar()
        self.store_address = tkinter.StringVar()
        self.item_name = tkinter.StringVar()
        self.item_price = tkinter.IntVar()
        self.item_count = tkinter.IntVar()
        self.id_store = tkinter.IntVar()
        self.list_box_stores = tkinter.StringVar(value=Store_Gui.list_stores)
        self.register_name = tkinter.StringVar()
        self.register_balance = tkinter.IntVar()
        
        self.create_objects()
    def __str__(self):
        return f'{Store_Gui.list_stores}'
        pass
        
    
    def create_objects(self):
        #create frames
        self.store_creation_frame = tkinter.Frame(self.main_window)
        self.inventory_management_frame = tkinter.Frame(self.main_window)
        self.register_frame = tkinter.Frame(self.main_window)
        self.order_frame =tkinter.Frame(self.main_window)
        self.dill_frame = tkinter.Frame(self.main_window)
        

        #create widgets store_creation_frame
        self.store_initialize_label_instance = ttk.Label(self.store_creation_frame,text="Enter instance name for new store: ")
        self.store_initialize_entry_instance = ttk.Entry(self.store_creation_frame,textvariable=self.instance, width = 15)
        self.store_initialize_label_city = ttk.Label(self.store_creation_frame,text="Enter city location of store being created: ")
        self.store_initialize_entry_city = ttk.Entry(self.store_creation_frame,textvariable=self.store_address, width = 15)

        self.store_initialize_button = ttk.Button(self.store_creation_frame,text="Create new store",command=self.create_store)
        self.store_store_idlist =ttk.Button(self.store_creation_frame,text="Provide store id",command=self.id_store_get)
        

        #pack widgets store_creation_frame
        self.store_initialize_label_instance.pack(side="left")
        self.store_initialize_entry_instance.pack(side="left")
        self.store_initialize_label_city.pack(side="left")
        self.store_initialize_entry_city.pack(side="left")
        self.store_initialize_button.pack(side="left")
        self.store_store_idlist.pack(side="left")
        

        #pack store_creation_frame frame
        self.store_creation_frame.pack()

        #create widgets inventory_management_frame
        self.display_stores_listbox = ttk.Combobox(self.inventory_management_frame,value='',postcommand = self.update_store_list)
        self.inventory_label_item = ttk.Label(self.inventory_management_frame,text="Item Name")
        self.inventory_entry_item = ttk.Entry(self.inventory_management_frame, textvariable=self.item_name, width=15)
        self.inventory_label_price = ttk.Label(self.inventory_management_frame,text="Item Price")
        self.inventory_entry_price = ttk.Entry(self.inventory_management_frame,textvariable=self.item_price, width=15)
        self.inventory_label_count = ttk.Label(self.inventory_management_frame,text="Item Count")
        self.inventory_entry_count = ttk.Entry(self.inventory_management_frame,textvariable=self.item_count, width=15)
        self.inventory_button = ttk.Button(self.inventory_management_frame,text="Add inventory item to store",command=self.add_item)
        self.inventory_button_get =ttk.Button(self.inventory_management_frame,text="Inventory Dicts",command=self.inventory_dict)
        self.store_update_name = ttk.Button(self.inventory_management_frame,text="Update Store Name",command=self.update_store_name)

        #pack widgets iventory management frame
        self.display_stores_listbox.pack(side="left")
        self.inventory_label_item.pack(side='left')
        self.inventory_entry_item.pack(side="left") 
        self.inventory_label_price.pack(side="left") 
        self.inventory_entry_price.pack(side="left") 
        self.inventory_label_count.pack(side="left") 
        self.inventory_entry_count.pack(side="left")
        self.inventory_button.pack(side="left")
        self.inventory_button_get.pack(side="left")
        self.store_update_name.pack(side="left")

        #pack inventory management frame
        self.inventory_management_frame.pack()

        #create register widgets
        self.register_label = ttk.Label(self.register_frame,text="Enter register name")
        self.register_entry = ttk.Entry(self.register_frame, width=15,textvariable=self.register_name)
        self.store_label = ttk.Label(self.register_frame,text="Select store to create register in")
        self.display_stores_cbox = ttk.Combobox(self.register_frame,value='',postcommand=self.update_store_list_register)
        self.register_balance_label = ttk.Label(self.register_frame,text="Enter starting balance of register")
        self.register_balance_entry = ttk.Entry(self.register_frame,width=5,textvariable=self.register_balance )
        self.register_add_button = ttk.Button(self.register_frame,text="Add new register",command=self.add_register)
        self.register_print_button = ttk.Button(self.register_frame,text="Print register list based on store address",command=self.print_registers)
        #pack register widgets
        self.register_label.pack(side="left")
        self.register_entry.pack(side="left")
        self.store_label.pack(side="left")
        self.display_stores_cbox.pack(side="left")
        self.register_balance_label.pack(side="left")
        self.register_balance_entry.pack(side="left")
        self.register_add_button.pack(side="left")
        self.register_print_button.pack(side="left")
        #pack frame
        self.register_frame.pack()

        #create order widgets
        self.order_store_label = ttk.Label(self.order_frame,text="Select Store to Order From")
        self.order_store_cb = ttk.Combobox(self.order_frame, value= "", postcommand=self.polulate_order_combo_store)
        self.order_registerid_label = ttk.Label(self.order_frame,text="Select register id for order")
        self.order_registerid_cb = ttk.Combobox(self.order_frame, value='',postcommand=self.update_register_cb)

        #pack widgets
        self.order_store_label.pack(side="left")
        self.order_store_cb.pack(side="left")
        self.order_registerid_label.pack(side="left")
        self.order_registerid_cb.pack(side="left")

        #pack frame
        self.order_frame.pack()

        #create button dill5
        self.dill_button = ttk.Button(self.dill_frame,text="Save Work",command=self.dill_run)
        #pack dill
        self.dill_button.pack()
        #pack frame
        self.dill_frame.pack()
    
    #this function generates Store dict on load for later use
    def polulate_order_combo_store(self):
        self.order_store_cb['values'] = []
        keys = Store.store_dict.keys()
        for location in keys:
            if location not in self.order_store_cb['values']:
                self.order_store_cb['values'] = tuple(list(self.display_stores_cbox['values']) + [location])
                
        
    
    def update_register_cb(self):
        self.order_registerid_cb['values'] = []
        location = self.order_store_cb.get()
        store_id = Store.store_dict[location]
        print(store_id)
        list_id = Store_Gui.register_dict[store_id]
        print(list_id)
        for id in list_id:
            self.order_registerid_cb['values'] = tuple(list(self.order_registerid_cb["values"]) + [id])

    def id_store_get(self):
        
        for item in Store_Gui.list_stores:
            Store.store_dict.update({item.store_address : item.store_id})
        string = Store.store_dict_get()
        tkinter.messagebox.showinfo('List store ids',f'{string}')
    def update_store_name(self):
        

        location = self.display_stores_listbox.get()
        storeid = Store.store_dict.get(location)
       
        address = simpledialog.askstring(title="Update Store name",prompt="Enter new store location: ")
      
        item = Store_Gui.list_stores[storeid]
        Store.store_location_set(item,address)
        

        Store.store_dict.update({address : storeid})
        Store.store_dict.pop(location)
        self.id_store_get()
    
    def print_registers(self):
        register = Store_Gui.register_dict
        tkinter.messagebox.showinfo('Registers by store_id and register_id',f'Store ID: [Register_ID] \n {register}')
        
    def create_store(self):
        create = self.instance.get()
        idstore = len(Store_Gui.id_stores)
        print(idstore)
        create = Inventory(self.store_address.get(),idstore)
        Store_Gui.list_stores.append(create)
        storeid = create.store_id_get()
        Store_Gui.id_stores.append(storeid)
        address = create.store_address_get()
        if address not in self.display_stores_listbox['values']:
            self.display_stores_listbox['values'] = tuple(list(self.display_stores_listbox['values']) + [address])
        
        
        string = Store.store_dict_get()
        tkinter.messagebox.showinfo('Entry Complete',f'Here is the updated store listing {string}')
        item = Store_Gui.list_stores
        
        self.instance.set('')
        self.store_address.set('')
        print(Store_Gui.id_stores)
    def inventory_dict(self):
        address = self.display_stores_listbox.get()
        id = Store.store_dict.get(address)
        print(id)

        inventory, price, address = Store_Gui.list_stores[int(id)].inventory_dict_get()
        tkinter.messagebox.showinfo("Dictionaries",f'Inventory: {inventory}\n Price: {price}\n Address: {address}')
    
    def dill_run(self):
        dill.dump_session("dump.pkl")


    
    def update_store_list(self):
        self.display_stores_listbox['values'] = []
        keys = Store.store_dict.keys()
        for location in keys:
            if location not in self.display_stores_listbox['values']:
                self.display_stores_listbox['values'] = tuple(list(self.display_stores_listbox['values']) + [location])
    def update_store_list_register(self):
        self.display_stores_cbox['values'] = []
        keys = Store.store_dict.keys()
        for location in keys:
            if location not in self.display_stores_cbox['values']:
                self.display_stores_cbox['values'] = tuple(list(self.display_stores_cbox['values']) + [location])
        
    def add_item(self):
        
        #get varaiables from entry boxes
        item = self.inventory_entry_item.get()
        price = self.inventory_entry_price.get()
        count = self.inventory_entry_count.get()

        location = self.display_stores_listbox.get()
        storeid = Store.store_dict.get(location)

        new_item = Store_Gui.list_stores[storeid].new_item(item,price,count)

        print(Store_Gui.list_stores[storeid].print_inventory_items())

        self.item_name.set('')
        self.item_price.set('')
        self.item_count.set('')
    def add_register(self):
        register_name = self.register_entry.get()
        cash_balance = self.register_balance_entry.get()
        store_address = self.display_stores_cbox.get()
        store_id = Store.store_dict[store_address]
        store_object = Store_Gui.list_stores[store_id]
        
        print(self.register_dict)
        register_id = len(Store_Gui.list_register)
        print(register_id)
        

        register_entry = Register(store_address,store_id,cash_balance,register_name,register_id)

        Store_Gui.registerid_instance_dict.update({register_id: register_entry})
        Store_Gui.list_register.append(register_entry)
        Store_Gui.id_register.append(register_id)
        
        if store_id in Store_Gui.register_dict:
            
            Store_Gui.register_dict[store_id].append(register_id)
        else:
            Store_Gui.register_dict.update({store_id: [register_id]})

        
        print(Store_Gui.register_dict,Store_Gui.registerid_instance_dict)

        
if __name__ == "__main__":
    main()