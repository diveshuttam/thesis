from scipy.interpolate import interp1d
import numpy as np
from math import ceil
from collections import deque
from old_sampling_test import byte_uniform


def periodic(x,y,a,k=100):
    periodic.__name__ = f"periodic with {(x[-1]-x[0])/k:.1f}s"
    return byte_uniform(x,y,k)


class window(deque):
    @property
    def mean(self):
        try:
            return sum(self)/len(self)
        except:
            return 0
    
    @property
    def stdev(self):
        try:
            return np.std(self)
        except:
            return 0

    @property
    def length(self):
        return len(self)

def cemon(x,y,a):
    x1,y1 = [],[]
    poller = a

    # initial variables
    current_time = x[0]
    τ = 1.0
    τ_max = 5.0
    τ_min = 0.5
    last_reading = 0
    win = window([])
    ws = 3
    

    while(current_time < x[-1]):
        current_reading = poller(current_time)
        x1.append(current_time)
        y1.append(current_reading)
        print(f"appending {current_time}, {current_reading}, τ = {τ}")
        var = current_reading-last_reading
        last_reading=current_reading
        if(win.length<3):
            current_time+=τ
            win.append(var)
            continue

        if(var>win.mean + 2*win.stdev or var<(win.mean - 2*win.stdev)):
            τ = max(τ_min,τ/2)
            ws = max(3,ceil(ws/2))
        else:
            τ = min(τ_max,τ*2)
            ws = ws + 1
        
        win.append(var)
        while win.length>ws:
            win.popleft()
        current_time += τ
    
    return x1,y1


def curvature(x,y,a):
    x1,y1 = [],[]
    poller = a

    # initial variables
    current_time = x[0]
    τ = 1.0
    τ_max = 5.0
    τ_min = 0.5
    last_reading = 0
    win_bytes = window([])
    dwin_bytes = window([])
    ddwin_bytes = window([])
    ws = 3
    

    while(current_time < x[-1]):
        current_reading = poller(current_time)
        x1.append(current_time)
        y1.append(current_reading)
        print(f"appending {current_time}, {current_reading}, τ = {τ}")
        var = current_reading-last_reading
        last_reading=current_reading
        if(win_bytes.length==0):
            current_time+=τ
            win_bytes.append(var)
            continue
        elif(win_bytes.length==1):
            current_time+=τ
            win_bytes.append(var)
            dwin_bytes.append((win_bytes[-1]-win_bytes[-2])/τ)
            continue
        win_bytes.append(var)
        dwin_bytes.append((win_bytes[-1]-win_bytes[-2])/τ)
        tdiff = (x[-1]+x[-2])/2.0 - (x[-2]+x[-3])/2.0
        ddwin_bytes.append((win_bytes[-1]-win_bytes[-3])/(tdiff))
        print(ddwin_bytes)
        if(ddwin_bytes[-1]>dwin_bytes.mean):
            τ = max(τ_min,τ/1.55)
            ws = max(3,ceil(ws))
        else:
            τ = min(τ_max,τ*2)
            ws = ws + 1
        
        while win_bytes.length>ws:
            win_bytes.popleft()
            ddwin_bytes.popleft()
            dwin_bytes.popleft()
        current_time += τ
    
    return x1,y1