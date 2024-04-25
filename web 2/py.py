import pandas as pd
import sqlite3
pd.set_option('display.max_rows', None)
conn = sqlite3.connect('prueba.db')

cursor = conn.cursor()


cursor.execute("SELECT * FROM vih")
_query="""
select * from vih 
"""
data = pd.read_sql_query(_query, conn)
print(data)


# data = cursor.fetchall()

# for i in data:
#     print(i)


# data=pd.read_csv("vih.csv")

# data.to_sql('vih', conn, if_exists='replace', index=False)

