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

        
        #create button dill5
        self.dill_button = ttk.Button(self.dill_frame,text="Save Work",command=self.dill_run)
        #pack dill
        self.dill_button.pack()
        #pack frame
        self.dill_frame.pack()
    #this function generates Store dict on load for later use
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
        
        address = self.display_stores_cbox.get()
        id = Store.store_dict.get(address)
        print(id)

        #store_instance = Register



        
        
        print(dict)
        
        tkinter.messagebox.showinfo("Registers",f'Store: {address}\n {dict}')

        
       
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
        register_id = len(self.register_dict)
        

        register_entry = Register(store_address,store_id,cash_balance,register_name,register_id)

        self.registerid_instance_dict.update({register_id: register_entry})
        
        if store_id in self.register_dict:
            
            self.register_dict[store_id].append(register_id)
        else:
            self.register_dict.update({store_id: [register_id]})

        
        print(self.register_dict,self.registerid_instance_dict)




        

    '''def create_order(self):
        #create inventory, price, address for store
        location = self.display_stores_cbox.get()
        storeid = Store.store_dict[location]
        store = Store_Gui.list_stores[int(storeid)]
        
        
        inventory, item, address = Inventory.inventory_dict_get(store)

        key_list = inventory.keys()

        order_dict = {}
        total = 0
        add_cart = -1
        for i in key_list:
            count = inventory[i]
            #while loop to make sure order is not over inventory
            while add_cart < 0 or add_cart > count:
                add_cart = int(simpledialog.askstring(title="Order Form",prompt="Enter quantity of {i} to order: "))
                
            order_dict.update({i : add_cart})
            add_cart = -1
        print(order_dict, inventory, item)
        sale = get_balance(order_dict, inventory, item, store)
        print(f"Your total is {sale: .2f}")
        balance = register.cash_balance_get()

        new_balance = sale + balance
        balance = register.cash_balance_set(new_balance)
        balance = register.cash_balance_get()
    def get_balance(self,order_dict, inventory, item,store):
        key_list = order_dict.keys()
        balance = 0
        for i in key_list:
            if order_dict[i] >0:
                price = item[i]
                count = order_dict[i]
                subtotal = price * count
                balance += subtotal
                inventory_new = inventory[i] - count
                Inventory.update_inventory_count(store,i,inventory_new)
        balance = balance*1.075
        
        return balance'''

        

        
if __name__ == "__main__":
    main()