from menu_item import MenuItem
from menu_manager import MenuManager

import psycopg2

#Connect to the database
DB_NAME = "Menu"
USER = "postgres" 
PASSWORD = "root" 
HOST = "localhost"
PORT = "5433" 

connection = psycopg2.connect(host=HOST, user=USER, password=PASSWORD, dbname=DB_NAME, port=PORT)
cursor = connection.cursor()

def show_user_menu():
    #shows program menu
    program_menu = input('''Type the letter for the program of your choice: 
    View an Item (V)
    Add an Item (A)
    Delete an Item (D)
    Update an Item (U)
    Show the Menu (S):  ''')

    #CANT CALL FUNCTIONS WITH NO ITEM OR PRICE INPUT
    if program_menu == 'V':
         #MenuManager.get_by_name()
         print('currently not an available option')
    elif program_menu == 'A':
        add_item_to_menu()
    elif program_menu == 'D':
        remove_item_from_menu()
    elif program_menu == 'U':
        update_item_from_menu()
    elif program_menu == 'S':
        show_restaurant_menu()
    else: 
        print('Your selection is not a valid option on the program menu')


def add_item_to_menu():
    item_name = input("enter item name: ")
    item_price = float(input("enter item price: "))

    MI = MenuItem(item_name, item_price)
    MI.save()
    #HOW TO CHECK IF SAVE WAS SUCCESSFULL ??
    print("item was added successfully")
    

def remove_item_from_menu():
    item_name = input("enter item name to be removed: ")
    #try:
    MI = MenuItem(item_name)
    MI.delete()
    #HOW TO CHECK IF SAVE WAS SUCCESSFULL ??
    print("item was deleted successfully")
    #except:
    #print("Error. Deleted item not complete")

def update_item_from_menu():
    item_name = input("enter item name to be updated: ")
    item_price = float(input("enter item price to be updated: "))
    new_name = input("enter new item name: ")
    new_price = float(input("enter new item name: "))
    #need to add IF item EXISTS situation else error message
    MI = MenuItem(item_name, item_price)
    MI.update(new_name, new_price)
    #HOW TO CHECK IF SAVE WAS SUCCESSFULL ??
    print("item was updated successfully")

def show_restaurant_menu():
    MM = MenuManager
    MM.all_items()
    
show_restaurant_menu()


test = show_user_menu()