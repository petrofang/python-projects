from inventory import InventoryItem
PROMPT='\n > '
inventory_list=[]

def print_menu():
    # print the user option menu
    menu=''
    menu+=('  (C)reate new inventory item\n')
    menu+=('  (P)rint out all items on the list\n')
    menu+=('  (#) display all information for inventory item #\n')
    menu+=(' e(X)it this program')
    return menu

def create_item():
    # create a new inventory item
    name=input('What is the new item called?'+PROMPT)
    wholesale_price=input(f'What is the wholesale cost of {name}?'+PROMPT)
    retail_price=input('and what will the retail price be?'+PROMPT)
    try:stock=int(input('What is the initial stock? Like how many?'+PROMPT))
    except:stock=0
    return InventoryItem(name, wholesale_price, retail_price, stock)

def print_inventory_list():
    # print the list of all items
    print(f'{f"#":^5}|{f"NAME":^20}')
    print(f'{"-"*5}+{"-"*20}')
    for item in inventory_list:
        print(f'{item.item_Number:^5}| {item.name}')
    print()


def main():
    while True:
        user_input=input(f'{print_menu()}{PROMPT}')
        if user_input.upper() == 'C': inventory_list.append(create_item())
        if user_input.upper() == 'P': 
           if inventory_list:  print_inventory_list() 
           else: print('There is no inventory, yet.')
        if user_input.upper() == 'X': exit()
        try: item_Number=int(user_input)
        except: pass
        else:
            if item_Number < 0: raise IndexError # stop messing around
            if item_Number < len(inventory_list): print(inventory_list[item_Number])
            else: raise IndexError 










if __name__=='__main__': main()