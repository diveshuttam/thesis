from scipy.interpolate import interp1d
import numpy as np
from math import ceil
from collections import deque
from old_sampling_test import byte_uniform


def periodic(x,y,bytes_poller, utilization_poller, k=100):
    periodic.__name__ = f"periodic with {(x[-1]-x[0])/k:.2f}s"
    return byte_uniform(x,y,k)

# def print(*args, **kwargs):
#     pass

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

def cemon(x,y,bytes_poller,utilization_poller, tmin, tmax, param):
    print("Cemon:")
    x1,y1,z1 = [],[],[]

    # initial variables
    current_time = x[0]
    τ = 1.0
    τ_max = tmax
    τ_min = tmin
    last_bytes = 0
    win = window([])
    ws = 3


    while(current_time < x[-1]):
        current_bytes = bytes_poller(current_time)
        x1.append(current_time)
        y1.append(current_bytes)
        try:
            current_utilization = utilization_poller(current_time)
            z1.append(current_utilization)
        except:
            print("breaking")
            break
        print(f"{current_time}, {current_bytes}, {τ}, ", end='')
        var = current_bytes-last_bytes
        last_bytes=current_bytes
        if(win.length<3):
            print(f'same, {τ}')
            current_time+=τ
            win.append(var)
            continue

        if((var>(win.mean + 2*win.stdev)) or (var<(win.mean - 2*win.stdev))):
            τ = max(τ_min,τ/2)
            ws = max(3,ceil(ws/2))
            print(f"double polling, {τ}")
        else:
            τ = min(τ_max,τ*2)
            ws = ws + 1
            print(f"halfing polling, {τ}")

        win.append(var)
        while win.length>ws:
            win.popleft()
        current_time += τ

    x1.append(x[-1])
    z1.append(utilization_poller(x[-1]))
    return x1,z1


def curvature(x,y,bytes_poller, utilization_poller, tmin, tmax, param):
    print("Curvature:")
    x1,y1,z1 = [],[],[]
    
    # initial variables
    current_time = x[0]
    τ = 1.0
    τ_max = tmax
    τ_min = tmin
    last_bytes = 0
    win_bytes = window([])
    dwin_bytes = window([])
    ddwin_bytes = window([])
    ws = 3

    previous=False
    while(current_time < x[-1]):
        current_bytes = bytes_poller(current_time)
        x1.append(current_time)
        y1.append(current_bytes)
        try:
            current_utilization = utilization_poller(current_time)
            z1.append(current_utilization)
        except:
            print("breaking")
            break
        print(f"{current_time}, {current_bytes}, {τ}, ", end='')
        # var = current_reading-last_reading
        last_bytes=current_bytes
        if(win_bytes.length==0):
            current_time+=τ
            win_bytes.append(current_bytes)
            print(f'same, {τ}')
            continue
        elif(win_bytes.length==1):
            current_time+=τ
            win_bytes.append(current_bytes)
            dwin_bytes.append((win_bytes[-1]-win_bytes[-2])/τ)
            print(f'same, {τ}')
            continue
        win_bytes.append(current_bytes)
        dwin_bytes.append((win_bytes[-1]-win_bytes[-2])/τ)
        tdiff = x1[-1]-x1[-3]
        ddwin_bytes.append((win_bytes[-1]-win_bytes[-3])/(tdiff))
        #instantaneous curvature
        # print(abs(ddwin_bytes[-1]-(dwin_bytes[-2]+dwin_bytes[-1])/2.0))
        # input()
        if(abs(dwin_bytes[-2]-dwin_bytes[-1])>param):
            print("increase", dwin_bytes[-2], dwin_bytes[-1], ddwin_bytes[-1])
            if(previous==False):
                τ = max(τ_min,τ/3.0)
                ws = max(3,ceil(ws))
                print(f"tripling polling, {τ}")
                previous=True
            else:
                print(f'same_p, {τ}')
        else:
            print("decrease", dwin_bytes[-2], dwin_bytes[-1], ddwin_bytes[-1])
            τ = min(τ_max,τ*2)
            print(f"halfing polling, {τ}")
            ws = ws + 1
            previous=False

        while win_bytes.length>ws:
            win_bytes.popleft()
            ddwin_bytes.popleft()
            dwin_bytes.popleft()
        current_time += τ

    x1.append(x[-1])
    z1.append(utilization_poller(x[-1]))
    return x1,z1

# def curvature2(x,y,bytes_poller, utilization_poller):
#     x1,y1 = [],[]
#     poller = bytes_poller

#     # initial variables
#     current_time = x[0]
#     τ = 1.0
#     τ_max = 5.0
#     τ_min = 0.5
#     last_reading = 0
#     win_bytes = window([])
#     dwin_bytes = window([])
#     ddwin_bytes = window([])
#     ws = 3

#     previous=False
#     while(current_time < x[-1]):
#         current_reading = poller(current_time)
#         x1.append(current_time)
#         y1.append(current_reading)
#         print(f"appending {current_time}, {current_reading}, τ = {τ}")
#         # var = current_reading-last_reading
#         last_reading=current_reading
#         if(win_bytes.length==0):
#             current_time+=τ
#             win_bytes.append(current_reading)
#             continue
#         elif(win_bytes.length==1):
#             current_time+=τ
#             win_bytes.append(current_reading)
#             dwin_bytes.append((win_bytes[-1]-win_bytes[-2])/τ)
#             continue
#         win_bytes.append(current_reading)
#         dwin_bytes.append((win_bytes[-1]-win_bytes[-2])/τ)
#         tdiff = x1[-1]-x1[-3]
#         ddwin_bytes.append((win_bytes[-1]-win_bytes[-3])/(tdiff))
#         #instantaneous curvature
#         print(abs(ddwin_bytes[-1]-(dwin_bytes[-2]+dwin_bytes[-1])/2.0))
#         # input()
#         kt = 1000
#         if(dwin_bytes[-1]-dwin_bytes[-2]>0):
#             if(previous==False):
#                 τ = max(τ_min,τ/3.0)
#                 ws = max(3,ceil(ws))
#                 previous=True
#         elif(dwin_bytes[-1]-dwin_bytes[-2] < 0):
#             τ = min(τ_max,τ*2)
#             ws = ws + 1
#             previous=False
#         else:
#             ws = ws + 1
#             previous=False
#             pass

#         while win_bytes.length>ws:
#             win_bytes.popleft()
#             ddwin_bytes.popleft()
#             dwin_bytes.popleft()
#         current_time += τ

#     return x1,y1


def momon(x,y,bytes_poller, utilization_poller, tmin, tmax, param):
    x1,y1,z1 = [],[],[]
    # initial variables
    current_time = x[0]
    τ = 1.0
    τ_max = tmax
    τ_min = tmin
    last_bytes = 0
    win = window([])
    ws = 3

    current_bytes=0
    while(current_time < x[-1]):
        last_bytes=current_bytes
        current_bytes = bytes_poller(current_time)
        x1.append(current_time)
        y1.append(current_bytes)
        print(f"appending {current_time}, {current_bytes}, τ = {τ}")
        try:
            utilization = utilization_poller(current_time)
        except:
            break
        z1.append(utilization)
        if(len(z1)<2):
            current_time+=τ
            continue
        un = z1[-1]
        un_1 = z1[-2]
        if (un+un_1!=0):
            dn = abs((un-un_1)/((un+un_1)/2.0))
        else:
            dn = 0
        if(win.length<2):
            current_time+=τ
            win.append(dn)
            continue
        win.append(utilization)
        if(abs(win[-1]-win[-2])>0.2):
            τ = max(τ_min,τ/2)
            # ws = max(3,ceil(ws/2))
        else:
            τ = min(τ_max,τ*3)
            # ws = ws + 1

        # win.append(utilization)
        # while win.length>ws:
            # win.popleft()
        current_time += τ
    x1.append(x[-1])
    z1.append(utilization_poller(x[-1]))
    
    return x1,z1


# def proportional(x,y,bytes_poller, utilization_poller):
#     x1,y1 = [],[]
#     poller = bytes_poller

#     # initial variables
#     current_time = x[0]
#     τ = 1.0
#     τ_max = 5.0
#     τ_min = 0.5
#     last_reading = 0
#     win = window([])
#     ws = 3

#     current_reading=0
#     while(current_time < x[-1]):
#         last_reading=current_reading
#         current_reading = poller(current_time)
#         x1.append(current_time)
#         y1.append(current_reading)
#         print(f"appending {current_time}, {current_reading}, τ = {τ}")
#         if(len(x1)<2):
#             current_time+=τ
#             continue
#         v=(y1[-1]-y1[0])/(x1[-1]-x1[0])
#         avg = (y1[-1]-y1[-2])/(x1[-1]-x1[-2])
#         τ = max(0.5,min(5.0,τ*v*1/(avg+1)))
#         current_time += τ

#     return x1,y1

# def ewma(x,y,bytes_poller,utilization_poller,α=0.5):
#     x1,y1 = [],[]
#     poller = bytes_poller

#     # initial variables
#     current_time = x[0]
#     τ_pt = 1.0
#     τ_ewma = 1.0
#     τ_max = 5.0
#     τ_min = 0.5
#     last_reading = 0
#     win = window([])
#     ws = 3

#     current_reading=0
#     while(current_time < x[-1]):
#         last_reading=current_reading
#         current_reading = poller(current_time)
#         x1.append(current_time)
#         y1.append(current_reading)
#         print(f"appending {current_time}, {current_reading}, τ = {τ_ewma}")
#         if(len(x1)<2):
#             current_time+=τ_ewma
#             continue
#         v=(y1[-1]-y1[0])/(x1[-1]-x1[0])
#         avg = (y1[-1]-y1[-2])/(x1[-1]-x1[-2])
#         τ_pt = max(0.5,min(5.0,τ_pt*v*1/(avg+1)))
#         τ_ewma = max(0.5,min(5.0,τ_pt*α + τ_ewma*(1-α)))
#         current_time += τ_ewma

#     return x1,y1
