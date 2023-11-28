class ItemToPurchase:
    def __init__(self, name='none', price=0, quantity=0, item_description="none"):
        self.item_name=name
        self.item_price=price
        self.item_quantity=quantity
        self.item_description=item_description

    def print_item_description(self):
        print(self.item_description)

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}')
    
    def __add__(self, other):
        if isinstance(other, ItemToPurchase):
            return self.item_price*self.item_quantity + other.item_price*other.item_quantity

class ShoppingCart:
    def __init__(self, customer_name='none', current_date='Janurary 1, 2016'):
        self.customer_name=customer_name
        self.current_date=current_date
        self.cart_items=[]
    
    def add_item(self, item:ItemToPurchase):
        self.cart_items.append(item)
    
    def remove_item(self, item:ItemToPurchase):
        if item in self.cart_items: self.cart_items.remove(item)

    def modify_item(self, item:ItemToPurchase):
        if item in self.cart_items: 
            '''If item can be found (by name) in cart, modify item in cart.'''
            pass # um, yay? modify it how???
        else:
            print('Item not found in cart. Nothing modified.')
    
    def get_num_items_in_cart(self):
        total_items=0
        for each_item in self.cart_items:
            total_items+=each_item.item_quantity
        return total_items 

    def get_cost_of_cart(self):
        sum=0
        for each in self.cart_items:
            sum+=each.item_price * each.item_quantity
        return sum
           # print(f'{each.item_name} {each.item_quantity} @ ${each.item_price} = ${each.item_price * each.item_quantity}')
  
    def print_total(self):
        if self.cart_items:
            print(f'{"total items in cart"}') #TODO: this
        else:
            print('SHOPPING CART IS EMPTY\n')
    
    def print_descriptions(self):
        if self.cart_items:
            for item in self.cart_items:
                print(f'{item.item_description}')

def print_menu():
    print('''MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
''')

def execute_menu(choice:str, my_cart:ShoppingCart):
    if choice == 'a':
        print('ADD ITEM TO CART')
        item_name=input('Enter the item name:\n')
        item_desc=input('Enter the item description:\n')
        item_price=int(input('Enter the item price:\n'))
        item_Qty=int(input("Enter the item quantity:\n"))
        print()
        my_cart.add_item(ItemToPurchase(item_name, item_price, item_Qty, item_desc))

    if choice == 'r': # Remove item from cart
        print('REMOVE ITEM FROM CART')
        item_name=input('Enter name of item to remove:\n')
        if item_name in [item.item_name for item in my_cart.cart_items]:
            item_index = [item.item_name for item in my_cart.cart_items].index(item_name)
            my_cart.cart_items.pop(item_index)
            print()
        else:
            print('Item not found in cart. Nothing removed.\n')

    if choice == 'c': # Change item quantity
        print("CHANGE ITEM QUANTITY")
        item_name=input('Enter the item name:\n')
        item_quantity=int(input('Enter the new quantity:\n'))
        if item_name in [item.item_name for item in my_cart.cart_items]:
            item_index = [item.item_name for item in my_cart.cart_items].index(item_name)
            my_cart.cart_items[item_index].item_quantity=item_quantity
        else:
            print('Item not found in cart. Nothing modified.\n')

    if choice == 'i': # Output items' descriptions
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{customer_name}'s Shopping Cart - {todays_date}\n")
        print(f"Item Descriptions")
        for item in my_cart.cart_items:
            print(f"{item.item_name}: {item.item_description}")
        print()

    if choice == 'o': # Output shopping cart
        print("OUTPUT SHOPPING CART")
        print(f"{my_cart.customer_name}'s Shopping Cart - {my_cart.current_date}")
        num_items=sum([item.item_quantity for item in my_cart.cart_items])
        print(f'Number of Items: {num_items}')
        print()
        if num_items > 0:
            for each_item in my_cart.cart_items:
                print(f'{each_item.item_name} {each_item.item_quantity} @ ${each_item.item_price} = ${each_item.item_quantity*each_item.item_price}')
        else: print('SHOPPING CART IS EMPTY')
        print(f'\nTotal: ${sum([item.item_quantity * item.item_price for item in my_cart.cart_items])}\n')
    if choice == 'q':
        quit()
    


def main(): 
    while True:
        print_menu()
        menu_choice=input('Choose an option:\n')
        while menu_choice not in menu_options:
            menu_choice=input('Choose an option:\n')
        execute_menu(menu_choice, shopping_cart)
    
if __name__ == "__main__":
    menu_options=['a','r','c','i','o','q']
    customer_name=input('Enter customer\'s name:\n')
    todays_date=input('Enter today\'s date:\n')
    print(f'\nCustomer name: {customer_name}')
    print(f'Today\'s date: {todays_date}\n')
    shopping_cart=ShoppingCart(customer_name, todays_date)
    main()