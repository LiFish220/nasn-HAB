# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 20:09:19 2021

@author: LiFish
"""
import pygame as pg
import weather
import count
import find
import time
import sys 

pg.init()
sys.setrecursionlimit(999999) 
running = True ; go = 0
main_clock = pg.time.Clock()

L = 0.0065 #Lapse rate of temperature  0.0065 K/m
M_air = 0.02897 #Molarcualr mass of air  0.02897 kg/mol
Rv = 0.0821 #
air_n = 29 #
P = 101300
pi = 3.14159265358979
Cd0 = 0.47
m_a = 5.131
R = 1
H = 0
ts = 0
sum_a = 0
x_b = 1
l_n = ""
g_mode = 0.004
screen = pg.display.set_mode((800,600)) #視窗大小
pg.display.set_caption('HAB final location predict')

back = pg.image.load("back.png")
white = pg.image.load("white.png")
hab = pg.image.load("hab.png")
b1 = pg.image.load("bt1.png")
b2 = pg.image.load("bt2.png")
go_t = pg.image.load("go.png")
bar = pg.image.load("bar.png")
s60 = pg.image.load("60s.png")

text = pg.font.SysFont('simhei', 32)
text2 = pg.font.SysFont('simhei', 90)
text3 = pg.font.SysFont('simhei', 24)
text4 = pg.font.SysFont('simhei', 56)

screen.blit(white,(0,0))
screen.blit(back,(0,0))
pg.display.update()

Temp,wind_d,wind_v = weather.get_T()
print(50)
re,c1,c2,c3 = weather.recommended(wind_v)
print(100)

T = count.temp(int(Temp))
H = 0
P1 = round(count.ground_pressure(P, L, H, T, M_air),1)
r1 = count.r(L,H,T,M_air)
V_z = count.V_z(r1)
m_g = round(count.m_g(P,V_z,T,g_mode),3)
m_l = 0.648
m_t = m_l + m_g
v1 = count.v_z(m_t,m_a,r1,Cd0)
A_p = round(count.air_pressure(1, air_n, Rv, T),3)
D = round(count.density(A_p, L, H, T, M_air),3)
sum_x = round(count.total_x(M_air, L, T, Cd0, R, m_t, m_a, 30000 ,wind_v),1)
t1 = int(count.need_time(M_air, L, T, Cd0, R, m_t, m_a, 10000))
t2 = int(count.need_time(M_air, L, T, Cd0, R, m_t, m_a, 20000))
t3 = int(count.need_time(M_air, L, T, Cd0, R, m_t, m_a, 30000))


text_box1 = text.render('Surface temperature:', True, (195, 195, 195),None)
text_box2 = text.render('Wind direction:', True, (195, 195, 195),None)
text_box3 = text.render('Wind speed:', True, (195, 195, 195),None)
text_box4 = text.render('Recommended level', True, (195, 195, 195),None)
text_box5 = text3.render('power by TURN TO TOP', True, (195, 195, 195),None)
text_box6 = text.render('Air temperature:', True, (195, 195, 195),None)
text_box7 = text.render('Ground pressure:', True, (195, 195, 195),None)
text_box8 = text.render('Altitude:', True, (195, 195, 195),None)
text_box9 = text.render('Elapsed time:', True, (195, 195, 195),None)
text_box10 = text.render('Progress:', True, (195, 195, 195),None)
text_box11 = text.render('10km', True, (195, 195, 195),None)
text_box12 = text.render('20km', True, (195, 195, 195),None)
text_box13 = text.render('30km', True, (195, 195, 195),None)
text_box14 = text.render(f'{t1}s', True, (195, 195, 195),None)
text_box15 = text.render(f'{t2}s', True, (195, 195, 195),None)
text_box16 = text.render(f'{t3}s', True, (195, 195, 195),None)
text_box17 = text.render('Rise speed:', True, (195, 195, 195),None)
text_box18 = text.render('Final location predict:', True, (195, 195, 195),None)
text_box19 = text.render('Distance:', True, (195, 195, 195),None)
text_box20 = text.render(f'{l_n}', True, (195, 195, 195),None)
text_box21 = text.render('0.002', True, (195, 195, 195),None)
text_box22 = text.render('0.004', True, (195, 195, 195),None)
text_box23 = text.render(f'total: {m_t}', True, (195, 195, 195),None)
text_box24 = text.render(f'load: {m_l}', True, (195, 195, 195),None)
text_box25 = text.render(f'gas: {m_g}', True, (195, 195, 195),None)

text_Temp = text2.render(f'{Temp}°C', True, (195, 195, 195),None)
text_Wind_d = text2.render(f'{wind_d}', True, (195, 195, 195),None)
text_Wind_v = text2.render(f'{wind_v}m/s', True, (195, 195, 195),None)
text_Level = text2.render(f'{re}',True, (c1,c2,c3),None)

while running:
    main_clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    for i in range(255,-1,-1):
        screen.blit(white,(0,0))
        back.set_alpha(i); screen.blit(back,(0,0)) ; pg.display.update() 
    break

hab.set_alpha(0);screen.blit(white,(0,0));screen.blit(hab,(400,15));time.sleep(0.1);pg.display.update()
hab.set_alpha(40);screen.blit(white,(0,0));screen.blit(hab,(400,15));time.sleep(0.1);pg.display.update()
hab.set_alpha(80);screen.blit(white,(0,0));screen.blit(hab,(400,15));time.sleep(0.1);pg.display.update()
hab.set_alpha(120);screen.blit(white,(0,0));screen.blit(hab,(400,15));time.sleep(0.1);pg.display.update()
hab.set_alpha(160);screen.blit(white,(0,0));screen.blit(hab,(400,15));time.sleep(0.1);pg.display.update()
hab.set_alpha(200);screen.blit(white,(0,0));screen.blit(hab,(400,15));time.sleep(0.1);pg.display.update()
hab.set_alpha(240);screen.blit(white,(0,0));screen.blit(hab,(400,15));time.sleep(0.1);pg.display.update()
b_t1 = 0 ; b_t2 = 0 ;b_t3 = 0

while running:
    T = count.temp(int(Temp))
    H = 0
    P1 = round(count.ground_pressure(P, L, H, T, M_air),1)
    r1 = count.r(L,H,T,M_air)
    V_z = count.V_z(r1)
    m_g = round(count.m_g(P,V_z,T,g_mode),3)
    m_t =round(m_l + m_g,3)
    g_time = count.get_time()
    main_clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    time_text = text.render(f'{g_time}', True, (195, 195, 195),None)
    screen.blit(white,(0,0)) ; screen.blit(time_text, (12,0)) ; screen.blit(hab,(400,20))
    screen.blit(text_box1,(130,120)) ; screen.blit(text_box2,(130,220)) ; screen.blit(text_box3,(130,320)) ; screen.blit(text_box4,(130,420)) ; screen.blit(text_box5,(600,570))
    screen.blit(text_Temp,(130,150)) ; screen.blit(text_Wind_d,(130,250)) ; screen.blit(text_Wind_v,(130,350)) ; screen.blit(text_Level,(130,450))
    
    text_box23 = text.render(f'total: {m_t}', True, (195, 195, 195),None)
    text_box24 = text.render(f'load: {m_l}', True, (195, 195, 195),None)
    text_box25 = text.render(f'gas: {m_g}', True, (195, 195, 195),None)
    
    user = pg.mouse.get_pos()
    x = user[0] ;y = user[1]
    mouse = pg.mouse.get_pressed()
    screen.blit(b1,(400,510))
    if 400 < x < 500 and 510 < y < 560:
        screen.blit(b2,(400,510))
        if mouse[0]:
          go = 1 ; break
    else:
        screen.blit(b1,(400,510))
    if 495 < x < 634 and 50 < y < 195:
        screen.blit(text_box21,(670,100))
        screen.blit(text_box22,(670,150))
        if mouse[0]:
            pg.draw.circle(screen,(195,195,195),(650,110),5)
            g_mode = 0.002 ; b_t1 = 1 ; b_t2 = 0
        if mouse[2]:
            pg.draw.circle(screen,(195,195,195),(650,160),5)
            g_mode = 0.004; b_t1 = 0 ; b_t2 = 1
            
    if 438 < y < 560 and 536 < x < 590:
        pg.draw.rect(screen, (195,195,195), [640, 439, 6, 120], 0)
        if mouse[0]:
            pg.draw.circle(screen,(88,88,88),(643,y),7)
            if 490 < y < 512:
                m_l = 0.648
            else:
                b_t3 = 1
                if y <490:
                    m_l = round(abs((490-y)*8.4*0.001+0.648),3)
                else:
                    m_l = round(abs((y-512)*8.4*0.001-0.648),3)
                    
            screen.blit(text_box23,(650,444)) ; screen.blit(text_box24,(650,484)) ;screen.blit(text_box25,(650,524))
            
    if b_t1:
        pg.draw.circle(screen,(195,195,195),(650,110),5)
        screen.blit(text_box21,(670,100))
    if b_t2:
        pg.draw.circle(screen,(195,195,195),(650,160),5)
        screen.blit(text_box22,(670,150))
    if b_t3:
         screen.blit(text_box23,(650,444))
    pg.display.update()

if go:
    
    running = True
    sum_a += int(t1/91)
    screen.blit(white,(0,0))
    try:
        loc_p = pg.image.load(find.get(sum_x,wind_d)+".png")
    except FileNotFoundError:
        loc_p = pg.image.load('sea.png')
    text_box26 = text.render(find.location_name(find.get(sum_x,wind_d)), True, (195, 195, 195),None)
    while running:
        main_clock.tick(1)
        g_time = count.get_time() 
        T = count.temp(int(Temp))
        H = round(ts*v1,1)
        r1 = count.r(L,H,T,M_air)
        v1 = round(count.v_z(m_t,m_a,r1,Cd0),1)
        if v1<0: v1 = 0.010
        A_p = round(count.air_pressure(1, air_n, Rv, T),3)
        D = round(count.density(A_p, L, H, T, M_air),3)
        P1 = round(count.ground_pressure(P, L, H, T, M_air),1)
        ts+=1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                
        time_text = text.render(f'{g_time}', True, (195, 195, 195),None)
        list_text = text.render(f'Temp: {Temp}°C    Wind_d: {wind_d}    Wind_v: {wind_v}m/s', True, (195, 195, 195),None)
        text_A_p = text2.render(f'{A_p}',True, (195, 195, 195),None)
        text_D = text2.render(f'{D}',True, (195, 195, 195),None)
        text_P1 = text2.render(f'{P1}',True, (195, 195, 195),None)
        text_H = text2.render(f'{H}',True, (195, 195, 195),None)
        text_T = text2.render(f'{ts}s',True, (195, 195, 195),None)
        text_v1 = text2.render(f'{v1}m/s',True, (195, 195, 195),None)
        text_K = text2.render(f'{round(T-L*H,2)}K',True, (195, 195, 195),None)
        text_S = text2.render(f'{sum_x}km',True, (195, 195, 195),None)

        screen.blit(white,(0,0)) ; screen.blit(time_text, (12,0)) ; screen.blit(list_text,(235,0))
        screen.blit(text_box6,(10,50)) ; screen.blit(text_box7,(10,150)) ; screen.blit(text_box8,(10,250)) ; screen.blit(text_box9,(10,350)) ; screen.blit(text_box5,(600,570))
        screen.blit(text_box10,(10,450)) ; screen.blit(text_box17,(300,50)) ; screen.blit(text_box18,(300,150)) ; screen.blit(text_box19,(520,50)) ;# screen.blit(text_box20,(300,250)) 
        screen.blit(text_box26,(300,430))
        
        screen.blit(text_K,(10,80)) ; screen.blit(text_P1,(10,180)) ; screen.blit(text_H,(10,280)) ; screen.blit(text_T,(10,380))
        screen.blit(bar,(10,510))  ; screen.blit(text_v1,(300,80)) ; screen.blit(loc_p,(300,180)) ; screen.blit(text_S,(520,80)) 
        
        if ts < t1:
            if ts >sum_a:
                x_b += 2
                sum_a +=int(t1/91)
            pg.draw.rect(screen, (195,195,195), [18, 517, x_b, 16], 0)
        elif ts < t2:
            if ts >sum_a:
                x_b += 2
                sum_a +=int(t1/120)
            pg.draw.rect(screen, (195,195,195), [18, 517, x_b, 16], 0)
        elif ts < t3:
            if ts >sum_a:
                x_b += 2
                sum_a +=int(t1/110)
            pg.draw.rect(screen, (195,195,195), [18, 517, x_b, 16], 0)
        else:
            pg.draw.rect(screen, (195,195,195), [18, 517, x_b, 16], 0)
                
        screen.blit(text_box11,(200,480)) ; screen.blit(text_box12,(440,480)) ; screen.blit(text_box13,(660,480)) 
        screen.blit(text_box14,(200,545)) ; screen.blit(text_box15,(440,545)) ; screen.blit(text_box16,(660,545))
        
        pg.display.update()
pg.quit()
