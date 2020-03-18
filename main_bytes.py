#!/usr/bin/env python3
import numpy
import os
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
import numpy as np
import sampling_schemes
from load_file import load_file
from similarity import *
import sys

def error(px,py,tx,ty):
    return dtw(px,py,tx,ty)

fname=sys.argv[1]
s1=sys.argv[2]
s2=sys.argv[3]

if(s1=="periodic"):
    p1= lambda : eval(sys.argv[4])
if(s2=="periodic"):
    p2= lambda : eval(sys.argv[5])

display_actual = True 
display_plot1 = True
display_plot2 = True

# load data and interpolate actual plot
arr = load_file(fname)
x,y = map(list,zip(*arr))
x = list(map(lambda zz:zz.timestamp(), x))
n = len(x)*2
a = interpolate.interp1d(x,y,'previous')
xc=np.linspace(x[0],x[-1],n)
targets = yc = a(xc)


# sampling1
sampling_scheme1 = eval(f"sampling_schemes.{s1}")
if(s1=="periodic"):
    x1,y1 = map(list,sampling_scheme1(x,y,a,p1()))
else:
    x1,y1 = map(list,sampling_scheme1(x,y,a))
print(len(x1),len(y1))

a1 = interpolate.interp1d(x1,y1,"linear")
x1c = np.linspace(x1[0],x1[-1],n)
predictions1 = y1c = a1(x1c)
error1 = error(x1,y1,x,y)
overhead1 = len(x1)

# sampling2 
sampling_scheme2 =  eval(f"sampling_schemes.{s2}")
if(s2=="periodic"):
    x2,y2 = map(list,sampling_scheme2(x,y,a,p2()))
else:
    x2,y2 = map(list,sampling_scheme2(x,y,a))
print(len(x2),len(y2))

a2 = interpolate.interp1d(x2,y2,"linear")
x2c = np.linspace(x2[0],x2[-1],n)
predictions2 = y2c = a2(x2c)
error2 = error(x2,y2,x,y)
overhead2 = len(x2)

# plot actual
if(display_actual):
    plt.plot(xc,yc,'r',label='actual data (interpolated)',markersize=1)

# plot 1
if(display_plot1):
    plt.plot(x1c,y1c,'g--',label=f'sampled data (interpolated) ({sampling_scheme1.__name__})', markersize=1)
    plt.plot(x1,y1,'go',label=f'sampled data ({sampling_scheme1.__name__})',markersize=4)

# plot 2
if(display_plot2):
    plt.plot(x2c,y2c,'b:',label=f'sampled data (interpolated) ({sampling_scheme2.__name__})', markersize=1)
    plt.plot(x2,y2,'bo',label=f'sampled data ({sampling_scheme2.__name__})',markersize=4)

# show plot
plt.suptitle(f"error green ({sampling_scheme1.__name__}): {error1} | overhead ({sampling_scheme1.__name__}): {overhead1} \n" 
             f"error blue ({sampling_scheme2.__name__}): {error2} | overhead ({sampling_scheme2.__name__}): {overhead2}")
plt.legend(loc="upper left")
plt.show()
