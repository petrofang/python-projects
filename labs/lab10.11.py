''' 10.11 LAB*: Program: Online shopping cart (Part 1) 

(1) Build the ItemToPurchase class with the following specifications:

Attributes (3 pts)
item_name (string)
item_price (int)
item_quantity (int)
Default constructor (1 pt)
Initializes item's name = "none", item's price = 0, item's quantity = 0
Method
print_item_cost()

Ex. of print_item_cost() output:

Bottled Water 10 @ $1 = $10
(2) In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class. (2 pts)

Ex:

Item 1
Enter the item name:
Chocolate Chips
Enter the item price:
3
Enter the item quantity:
1

Item 2
Enter the item name:
Bottled Water
Enter the item price:
1
Enter the item quantity:
10

(3) Add the costs of the two items together and output the total cost. (2 pts)

Ex:

TOTAL COST
Chocolate Chips 1 @ $3 = $3
Bottled Water 10 @ $1 = $10

Total: $13
'''

class ItemToPurchase:
    def __init__(self, name='none', price=0, quantity=0):
        self.item_name=name
        self.item_price=price
        self.item_quantity=quantity

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}')
    
    def __add__(self, other):
        if isinstance(other, ItemToPurchase):
            return self.item_price*self.item_quantity+other.item_price*other.item_quantity


    
def main(): 
    print('Item 1')
    item1name=input('Enter the item name:\n')
    item1price=int(input('Enter the item price:\n'))
    item1Qty=int(input("Enter the item quantity:\n"))
    print('\nItem 2')
    item2name=input('Enter the item name:\n')
    item2price=int(input('Enter the item price:\n'))
    item2Qty=int(input("Enter the item quantity:\n"))
    item1=ItemToPurchase(item1name, item1price, item1Qty)
    item2=ItemToPurchase(item2name, item2price, item2Qty)
    print('\nTOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print(f'\nTotal: ${item1+item2}')

if __name__ == "__main__":main()