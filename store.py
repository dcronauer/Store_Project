#purpose of this code is to make a store app with the following functionality
# 1) store(within each store want orders, inventory, employees to start)

#create store
class Store:
    store_dict = {}
   
    def __init__(self,store_id,store_address):
        self.store_id = store_id
        self.store_address = store_address
        Store.store_dict.update({self.store_id : self.store_address})
        
    #store get and set
    def store_id_get(self):
        return self.store_id
    def store_address_get(self):
        return self.store_address
    def store_id_set(self,store_id):
        self.store_id = store_id
    def store_address(self,store_address):
        self.store_address = store_address
    def store_dict_get():
        return Store.store_dict
   
#create inventory for store instance   
class Inventory(Store):
    def __init__(self,store_id,store_address):
        super().__init__(store_id,store_address)
        self.inventory_dict = {}
        self.item_dict = {}
       
        
    #mutators item and inventory
    def new_item(self,item ,price, count):
        self.inventory_dict.update({item : count})
        self.item_dict.update({item : price})
    def item_remove(self,item):
        self.inventory_dict.pop(item)
        self.item_dict.pop(item)
    def update_inventory_count(self,item,count):
        self.inventory_dict.update({item: count})
     #dictionary calls
    def inventory_dict_get(self):
        return self.inventory_dict, self.item_dict, self.store_address
    #accesors item and inventory
    def print_inventory_items(self):
        return self.inventory_dict
        
class Register(Inventory):
    def __init__(self,store_id,store_address,cash_balance):
        super().__init__(store_id,store_address)
        self.cash_balance = cash_balance
        
    #accessors    
    def cash_balance_get(self):
        return self.cash_balance
    
    #mutators
    def cash_balance_set(self,cash_balance):
        self.cash_balance = cash_balance
    
        
def create_order(store, register):
    #create inventory, price, address for store
    inventory, item, address = Inventory.inventory_dict_get(store)
    
    key_list = inventory.keys()
    
    order_dict = {}
    total = 0
    add_cart = -1
    for i in key_list:
        count = inventory[i]
        #while loop to make sure order is not over inventory
        while add_cart < 0 or add_cart > count:
            add_cart = int(input(f'How many {i} do you want, current stock is {count}:'))
            
        order_dict.update({i : add_cart})
        add_cart = -1
    print(order_dict, inventory, item)
    sale = get_balance(order_dict, inventory, item,store)
    print(f"Your total is {sale: .2f}")
    balance = register.cash_balance_get()
    
    new_balance = sale + balance
   
    balance = register.cash_balance_set(new_balance)
    balance = register.cash_balance_get()
    
    
def get_balance(order_dict, inventory, item,store):
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
    
    return balance

def main():
    #create stores with inventory
    list_stores = []
    Store1 = Inventory(1,"Springfield")
    list_stores.append(Store1)
    Store2 = Inventory(2,"Marysville")
    list_stores.append(Store2)
    Store3 = Inventory(3,"Columbus")
    list_stores.append(Store3)
    
    #create register
    Register1 = Register(1,"Springfield", 500)

    #add inventory to stores (add desc, price, count)
    Store1.new_item("Lipstick",7.50,50)
    Store1.new_item("Dress",50,5)
    Store1.new_item("Bra", 25, 15)
    Store2.new_item("Chair",25,10)
    Store3.new_item("Desk",100,2)
    
    #create order 
    create_order(Store1, Register1)
    
    #get new inventory and new cash balance
    print(Store1.print_inventory_items())
    print(Register1.cash_balance_get())
    
   
    '''#print inventory information for each store
    for i in list_stores:
        inventory, item, address = Inventory.inventory_dict_get(i)
        print(f'Please see the price list for store at location {address}', item)
        print('')
        print(f'Please see the count list for store at location {address}', inventory)
        print('')
        print(Store.store_dict_get())'''
if __name__ == "__main__":    
    main()