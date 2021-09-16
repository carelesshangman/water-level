import mysql.connector
from serial.tools.list_ports_windows import NULL 
from datetime import datetime

now = datetime.now()

dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="waterlevel"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT MAX(ID) FROM level WHERE ID > 0")
idMax = mycursor.fetchall()

newIDcnv = str(idMax[0])[1:-2]

newID = int(newIDcnv) + 1

print(newID)

query = "INSERT INTO level (ID,wLevel,date) VALUES (%s,%s,%s)"

waterLevel = input("insert water level: ")

a = (newID,waterLevel,dt_string)
mycursor.execute(query,a)
mydb.commit()
