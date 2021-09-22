import pandas as pd
import json
import sqlite3


# Open JSON data and load on dataframe
with open("dev\city_database\city_list.json", errors="ignore", encoding='utf-8') as f:
    data = json.load(f)

f.close()

df = pd.DataFrame(data)
df = df.applymap(str) #convert all data to str to avoid unsupported type

# print(df)

connect = sqlite3.connect("data.db")
cursor = connect.cursor()

cursor.execute("""DROP TABLE IF EXISTS city_list""")

# cursor.execute("""DROP TABLE IF EXISTS city_list""")

df.to_sql("city_list",connect)

# clean entries with blank contries
cursor.execute("""
        DELETE FROM city_list WHERE country = ''
""")


