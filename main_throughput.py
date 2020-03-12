#!/usr/bin/env python3
import numpy
import os
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
import numpy as np
import sampling_schemes
from load_file import load_file
import similaritymeasures
from similarity import *
import sys

def error(px,py,tx,ty):
    return rmse(px,py,tx,ty)

display_actual = True 
display_plot1 = True
display_plot2 = True

fname=sys.argv[1]
s1=sys.argv[2]
s2=sys.argv[3]
interval=float(sys.argv[4])
if(s1=="periodic"):
    p1= lambda : eval(sys.argv[5])
if(s2=="periodic"):
    p2= lambda : eval(sys.argv[6])

# load data and interpolate actual plot
arr = load_file(fname)
x,y = map(list,zip(*arr))
x = list(map(lambda zz:zz.timestamp(), x))
n = len(x)*2
a = interpolate.interp1d(x,y,'previous',fill_value='extrapolate')
xct=np.linspace(x[0],x[-1],n)
targets = yct = a(xct+interval) -a(xct)

# our scheme
sampling_scheme1 = eval(f"sampling_schemes.{s1}") 
if(s1=="periodic"):
    x1,y1 = map(list,sampling_scheme1(x,y,a,p1()))
else:
    x1,y1 = map(list,sampling_scheme1(x,y,a))
x1t = x1
y1t = a(np.array(x1)+interval)-a(np.array(x1))
s1_name = sampling_scheme1.__name__
print(len(x1),len(y1))

a1 = interpolate.interp1d(x1t,y1t,"linear")
x1c = np.linspace(x1[0],x1[-1],n)
predictions1 = y1c = a1(x1c)
error1 = error(x1t,y1t,xct,yct)
overhead1 = len(x1)

# cemon
sampling_scheme2 = eval(f"sampling_schemes.{s2}")
if(s2=="periodic"):
    x2,y2 = map(list,sampling_scheme2(x,y,a,p2()))
    print("here")
else:
    x2,y2 = map(list,sampling_scheme2(x,y,a))
s2_name = sampling_scheme2.__name__

# calculate throughput
x2t = x2
y2t = a(np.array(x2)+interval)-a(np.array(x2))
print(len(x2),len(y2))

# interpolate throughput
a2 = interpolate.interp1d(x2t,y2t,"linear")
x2c = np.linspace(x2[0],x2[-1],n)
predictions2 = y2c = a2(x2c)
error2 = error(x2t,y2t,xct,yct)
overhead2 = len(x2)

# plot actual
if(display_actual):
    plt.plot(xct,yct,'r',label='actual data (interpolated)',markersize=1)

# plot 1
if(display_plot1):
    plt.plot(x1c,y1c,'g--',label='sampled data (our scheme)', markersize=1)
    plt.plot(x1t,y1t,'go',label='sampled data (interpolated) (our scheme)',markersize=4)

# plot 2
if(display_plot2):
    plt.plot(x2c,y2c,'b:',label='sampled data (cemon)', markersize=1)
    plt.plot(x2t,y2t,'bo',label='sampled data (interpolated) (cemon)',markersize=4)

# show plot
plt.suptitle(f"error green ({s1_name}): {error1} | overhead ({s1_name}): {overhead1} \n" 
             f"error blue ({s2_name}): {error2} | overhead ({s2_name}): {overhead2}")
plt.legend(loc="upper left")
plt.show()
