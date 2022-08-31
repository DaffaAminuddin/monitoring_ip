import csv
import MySQLdb
import time
print('csv to sql running')
mydb = MySQLdb.connect(host="127.0.0.1", user="admin", password="s0t0kudus", database="monitoring")

with open('persons.csv') as csv_files:
    csvfile = csv.reader(csv_files, delimiter=',')
    all_value= []
    for row in csvfile:
        value = (row[0], row[1], row[2])
        all_value.append(value)

query = "INSERT INTO monitoring_ip (IP,Status,Date) VALUES (%s,%s,%s)"

mycursor = mydb.cursor()
mycursor.executemany(query, all_value)
mydb.commit()
