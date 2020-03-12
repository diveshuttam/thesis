import similaritymeasures
import numpy as np
import scipy.interpolate as interpolate

def rmse(px,py,tx,ty):
    pf = interpolate.interp1d(px,py,"linear")
    tf = interpolate.interp1d(tx,ty,"linear")
    n=len(tx)*5
    xc=np.linspace(px[0],px[-1],n)
    p=pf(xc)
    t=tf(xc)
    return np.sqrt(np.average(((p-t)**2)))

def dtw(px,py,tx,ty):
    p=np.array(list(zip(px,py)))
    t=np.array(list(zip(tx,ty)))
    return similaritymeasures.dtw(t,p)[0]
