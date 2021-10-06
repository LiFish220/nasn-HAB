# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:43:59 2021

@author: LiFish
"""
import serial
import datetime
import time
import psutil

def setup(): #設備整頓
    global ser , wks , data , sheet
    COM_PORT = "COM14"
    BAUD_RATES = "9600"
    ser = serial.Serial(COM_PORT,BAUD_RATES)
    print("ser:",True)
    open('data.txt','w')

def get_time(): #時間接收
    a = datetime.datetime.now()
    b = str(a)
    return b[:19]

def read_data(): #讀取Arduino相關訊息
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
        
 
def save(t,y1,y2,y3): #寫入txt
    a = open('data.txt','a')
    a.write(f'{t}#{y1}#{y2}#{y3}')
    a.close()
    
def ser_type(x=0): #serial模組相關設定
    if x == 0:
        ser.open()
    else:
        ser.close()

def get_type(): #設備cpu、ram監測
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
