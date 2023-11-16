class InventoryItem:
    item_Number=0 # do we really want the end-user setting item_number?
    # it's a unique identifier right? I'm just gonna put it here.
    def __init__(self, name:str, wholesale_price=0.0, retail_price=0.0, quantity_in_stock=0):
        self.item_Number=InventoryItem.item_Number 
        InventoryItem.item_Number+=1
        # the item_Number will be the same as the list index in main.py
        # assuming all InventoryItems are added to list when they are instantiated    
        self.name=name 
        self.wholesale_price=wholesale_price 
        self.retail_price=retail_price
        self.quantity_in_stock=quantity_in_stock

    def __str__(self): 
        items=''
        # generate a nice-ish looking table of the item's properties
        for key,val in self.__dict__.items(): items+= f'{key:<20}: {val}\n'
        return items

    def print(self):print(self)
        # so we can item.print()

    def shipment(self, howmany):
        #incoming shipment - restock time
        self.quantity_in_stock+=howmany

    def purchased(self, howmany):
        # outgoing shipment.. UPS time
        if howmany <= self.quantity_in_stock:
            self.quantity_in_stock -=howmany
        else: pass # should we print a warning? raise an error?

def main():
    windoze=InventoryItem('Windows 11 Professional Edition', 40, 100, 600)
    windoze.print()
    windoze.shipment(20)
    windoze.print()
    windoze.purchased(20)
    windoze.print()

if __name__=="__main__":main()