# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:43:59 2021

@author: LiFish
"""
import serial
import datetime
import time
import psutil

def setup():
    global ser , wks , data , sheet
    COM_PORT = "COM14"
    BAUD_RATES = "9600"
    ser = serial.Serial(COM_PORT,BAUD_RATES)
    print("ser:",True)
    open('data.txt','w')

def get_time():
    a = datetime.datetime.now()
    b = str(a)
    return b[:19]

def read_data():
    i = 0
    while True:
        a = ser.readline() ; data = a.decode()
        d = data.strip('ppm').strip('co2').strip('：').strip('#')
        co2_list = [];co_list = [] ; temp_list = []
        if i ==0:
            co2_list.append(d)
        elif i ==1:
            co_list.append(d)
        else:
            temp_list.append(d)
            break
    return(co2_list[0],co_list[0],temp_list[0])
        
 
def save(t,y1,y2,y3):
    a = open('data.txt','a')
    a.write(f'{t}#{y1}#{y2}#{y3}')
    a.close()
    
def ser_type(x=0):
    if x == 0:
        ser.open()
    else:
        ser.close()

def get_type():
   cpu = psutil.cpu_percent()
   ram = psutil.virtual_memory().percent
   return (cpu,ram)

print(get_type())

if __name__ == '__main__':
    setup()
    while True:
        try:
            n_time = get_time()
            cpu,ram = get_type()
            Co2,Co,Temp = read_data()
            save(n_time, Co2, Co, Temp)
            print(n_time,Co2,Co,Temp,cpu,ram)
            time.sleep(1)
        except KeyboardInterrupt:
            ser_type(1)
            break
