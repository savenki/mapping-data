import sqlite3

from matplotlib.pyplot import table
from numpy import insert
cx = sqlite3.connect("test.sqlite")
table = 'CREATE TABLE people(id integer primary key, name Text, surname Text) '
cursor = cx.cursor()
cursor.execute(table)
cx.commit()
cx.close()