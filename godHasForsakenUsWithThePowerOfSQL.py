import serial.tools.list_ports
import mysql.connector
from serial.tools.list_ports_windows import NULL 
from datetime import datetime
#datetime logic
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
#serial read logic
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []
#read ports and select port logic
for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))
val = input("enter port: COM")
#select port for use
for x in range(0,len(portList)):
    if portList[x].startswith("COM"+str(val)):
        portVar="COM" + str(val)
        print(portList[x])
#quick init for port
serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
#init sql base
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="waterlevel"
)
#init cursor and ID
mycursor = mydb.cursor()

#read serial data
while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        sensorValue = packet.decode('utf').rstrip('\n')
        print(sensorValue)
        mycursor.execute("SELECT MAX(ID) FROM level WHERE ID > 0")
        idMax = mycursor.fetchall()
        newIDcnv = str(idMax[0])[1:-2]
        newID = int(newIDcnv) + 1
        query = "INSERT INTO level (ID,wLevel,date) VALUES (%s,%s,%s)"
        a = (newID,sensorValue,dt_string)
        mycursor.execute(query,a)
        mydb.commit()
