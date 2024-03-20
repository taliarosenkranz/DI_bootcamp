import psycopg2

#Connect to the database

DB_NAME = "Menu"
USER = "postgres" 
PASSWORD = "root" 
HOST = "localhost"
PORT = "5433" 

connection = psycopg2.connect(host=HOST, user=USER, password=PASSWORD, dbname=DB_NAME, port=PORT)
cursor = connection.cursor()

class MenuItem:
    def __init__(self, name, price=0, table_name='Menu_Items'):
        self.name = name
        self.price = price
        self.table_name=table_name
        
    def save(self):
        save = f'''INSERT INTO {self.table_name} (item_name, item_price) VALUES ('{self.name}', {self.price})'''
        cursor.execute(save) # execute the query
        connection.commit() # make changes in the database
       

    def delete(self):
        delete = f'''DELETE FROM {self.table_name} WHERE item_name = '{self.name}' '''
        cursor.execute(delete) 
        connection.commit() 
        
    def update(self, new_name, new_price):
        update_name = f'''UPDATE {self.table_name}
        SET item_name = '{new_name}', item_price = {new_price}
        WHERE item_name = '{self.name}' 
        AND item_price = {self.price} '''
        
        cursor.execute(update_name) 
        connection.commit() 
  

    def close_connection():
        connection.close()


item = MenuItem('Burger', 35)
item.save()
item.update('Veggie Burger', 37)
item.delete()
#item.close_connection()