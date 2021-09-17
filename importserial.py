import serial.tools.list_ports
import mysql.connector
from serial.tools.list_ports_windows import NULL 
from datetime import datetime
import time

serialcomm = serial.Serial('COM3', 9600)

serialcomm.timeout = 1

while True:

    print(serialcomm.readline().decode('ascii'))
    packet = serialcomm.readline()
    sensorValue = packet.decode('utf').rstrip('\n')
    print(sensorValue)

    if int(sensorValue) < 8:
        i="on"
    else:
        i="off"

    serialcomm.write(i.encode())

    time.sleep(0.5)

serialcomm.close()