import pandas as pd
import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

data = pd.read_csv('titles.csv')
df = pd.DataFrame(data)
res = df.to_sql(name="titles", con=con, if_exists="replace")

data = pd.read_csv('credits.csv')
df = pd.DataFrame(data)
res = df.to_sql(name="credits", con=con, if_exists="replace")
