#purpose of this code is to make a store app with the following functionality
# 1) store(within each store want orders, inventory, employees to start)

#create store
class Store:
    def __init__(self,store_id,store_address):
        self.store_id = store_id
        self.store_address = store_address
        self.inventory_dict = {}
        self.orders_dict = {}
        self.employees_dict = {}
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
    #accesors item and inventory
    def print_inventory_items(self):
        print(self.inventory_dict)
        print(self.item_dict)
    #store get and set
    def store_id_get(self):
        return self.store_id
    def store_address_get(self):
        return self.store_address
    def store_id_set(self,store_id):
        self.store_id = store_id
    def store_address(self,store_address):
        self.store_address = store_address
    #dictionary calls
    def inventory_dict_get(self):
        return self.inventory_dict, self.item_dict
def main():
    entry = Store(1,"Springfield")
    
    print(entry.store_id_get())
    print(entry.store_address_get())
    inventory, item = Store.inventory_dict_get(entry)
    print( item, inventory)
    
main()
    