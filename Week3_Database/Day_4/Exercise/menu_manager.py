import psycopg2

#Connect to the database

DB_NAME = "Menu"
USER = "postgres" 
PASSWORD = "root" 
HOST = "localhost"
PORT = "5433" 

connection = psycopg2.connect(host=HOST, user=USER, password=PASSWORD, dbname=DB_NAME, port=PORT)
cursor = connection.cursor()

class MenuManager:
    def __init__():
        pass
    
    def get_by_name(specific_item):
        
        query = f''' SELECT item_name 
        FROM Menu_Items
        WHERE item_name = '{specific_item}' '''
        cursor.execute(query) 
        results = cursor.fetchall()
        if len(results) == 0:
            print(None)
        return results
        
    
    def all_items():
        all_items = f''' SELECT * FROM Menu_Items'''
        cursor.execute(all_items) 
        results = cursor.fetchall()  
        print(results)
#def close_connection():
    #connection.close()

item2 = MenuManager.get_by_name('Beef Stew')
items = MenuManager.all_items()

#close = close_connection()