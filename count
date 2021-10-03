# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 15:34:52 2021

@author: LiFish
"""

import datetime
import random 

L = 0.0065 #Lapse rate of temperature  0.0065 K/m
M_air = 0.02897 #Molarcualr mass of air  0.02897 kg/mol
R = 0.0821 #
air_n = 29 #
P = 101300
pi = 3.14159265358979
Cd0 = 0.47
m_t = 1.810
m_a = 5.131
H = 0
R = 1

def m_g(P,V_z,T,g_mode):
    return (P*V_z/8.314/T)*g_mode

def air_pressure(P,n,R,T):
    return(P*n)/(R*T)

def density(A_p,L,H,T,M):
    return A_p*(1-(L*H)/T)**(9.8*M/8.314/L-1)

def temp(c):
    return (c+273.15)

def ground_pressure(P,L,H,T,M):
    return P*(1-(L*H)/T)**(9.8*M/8.314/L)

def V_z(H):
    return 4/3*pi*H**3

def r(L,H,T,M):
    return (1-(L*H)/T)**(1/3*(1-9.8*M/8.314/L))

def v_z(m_t,m_a,R,Cd0):
    return ((1-m_t/m_a)*8*R*9.8/3/Cd0)**0.5

def need_time(M,L,T,Cd0,R,m_t,m_a,H):
    return (1/6*(9.8*M/8.314/L-1)+1)**(-1)*(T/L)*(3*Cd0/8/R/9.8/(1-m_t/m_a))**0.5*(1-(1-L/T*H)**(1/6*(9.8*M/8.314/L-1)+1))

def get_time():
    a = datetime.datetime.now()
    b = str(a)
    return b[:19]
def wind_speed(x,H):
    if H < 1000:
        return(random.uniform(x, x+7))
    elif H <2000:
        return(random.uniform(x+5, x+10))
    elif H <3000:
        return(random.uniform(x+7, x+13))
    elif H <5000:
        return(random.uniform(x+8, x+17))
    elif H <7000:
        return(random.uniform(x+17, x+22))
    elif H <8000:
        return(random.uniform(x+20, x+33))
    elif H <10000:
        return(random.uniform(x+33, x+45))
    elif H <11000:
        return(random.uniform(x+20, x+37))
    elif H <13000:
        return(random.uniform(x+13, x+20))
    elif H <16000:
        return(random.uniform(x+5, x+11))
    else:
        return(random.uniform(x+2, x+6))

def a(Cd0,A_p,pi,R,V,a,t):
    return 0.5*Cd0*A_p*pi*(R)**2*(V-a*t)**2

def d_x(a,t):
    v = a*t
    return (v*t)/2

def total_x(M_air, L, T, Cd0, R, m_t, m_a, H ,V):
    sum_x = 0
    t = need_time(M_air, L, T, Cd0, R, m_t, m_a, H)
    ma = a(Cd0,A_p,pi,R,V,0,1)
    v1 = v_z(m_t,m_a,r1,Cd0)
    for i in range(int(t+1)):
        w_v = wind_speed(V, v1*i)
        ma = a(Cd0,A_p,pi,R,w_v,ma,0.01)
        t_x = d_x(ma,1)
        sum_x += t_x
        #print(ma,w_v)
    return sum_x/1000
