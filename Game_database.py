
import sqLite3
import time
import datetime
import random

conn = sqLite3.connect('game.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datastamp TEXT, keywork TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(4234332, '08-02-2016' , 'python, 8)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyord, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyowrd, value))
    conn.commit()

def read_from_db():
    #c.execute('SELECT * FROM stuffToPlot')
    #data = c.fetchall()
    for row in c.fetchall():
    print(row)
    




#create_tale()
#data_entry()
#for i in range(10):
#   dynamic_data_entry()
#   time.sleep(1)
read_from_db()
c.close()
conn.close()

