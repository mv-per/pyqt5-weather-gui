


import sqlite3

class weatherGUI_database:

    def __init__(self, database, table):

        self.__country = None
        self.__city = None
        self.connection = sqlite3.connect(database) #1st run : it created the mydata.db file; 2nd run: it only connected
        self.cursor = self.connection.cursor()
        self.table = table

    def load_countries(self):
        
        self.cursor.execute(f"""
            SELECT DISTINCT country FROM {self.table}        
        """)
        countries = self.cursor.fetchall()
        countries = [str(x[0]) for x in countries]
        countries.sort()
        return countries


    def load_cities(self, country):
        self.cursor.execute(f"""
            SELECT name FROM {self.table} WHERE country = '{country}'        
        """)
        cities = self.cursor.fetchall()
        cities = [str(x[0]) for x in cities]
        cities.sort()
        return cities

    def load_city_id(self, city, country):
        self.cursor.execute(f"""
            SELECT id FROM {self.table} WHERE country = '{country}' AND name = '{city}'        
        """)
        id = self.cursor.fetchone()
        # print(id)
        return id[0]


# city = city_db("dev\city_database\data.db", "city_list")

# # city.load_countries()

# # city.load_cities("BR")

# city.load_city_id("Toledo", "US")
# city.load_city_id("Toledo", "ES")
# city.load_city_id("Toledo", "BR")

if __name__ == "main":
    pass