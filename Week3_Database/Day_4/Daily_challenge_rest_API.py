import requests
import random
import psycopg2 

#Connect to the database
DB_NAME = "RestAPI"
USER = "postgres" 
PASSWORD = "root" 
HOST = "localhost"
PORT = "5433" 

connection = psycopg2.connect(host=HOST, user=USER, password=PASSWORD, dbname=DB_NAME, port=PORT)


def get_countries():
    response = requests.get('https://restcountries.com/v3.1/all')
    if response.status_code == 200:
        return response.json()
    else:
        return None

def select_random_countries(countries, num_countries=10):
    return random.sample(countries, num_countries)

def write_to_database(countries, connection=connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE rest_countries")
    cursor.execute("CREATE TABLE rest_countries (name varchar(50), capital varchar(50), flag BYTEA, subregion varchar(50), population integer)")
    for country in countries:
        cursor.execute("INSERT INTO rest_countries (name, capital, flag, subregion, population) VALUES (%s, %s, %s, %s, %s)",  (country['name']['common'], country['capital'], country['flag'], country['subregion'], country['population']))

                    
    connection.commit()
    cursor.close()
    connection.close()

def main():
    countries_data = get_countries()
    #print(f'here are the countries_data{countries_data}')
    if countries_data:
        random_countries = select_random_countries(countries_data)
        write_to_database(random_countries) 
        print("10 random countries written to the database.")
    else:
        print("Failed to retrieve data from the API.")

if __name__ == "__main__":
    main()