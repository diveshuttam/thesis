import similaritymeasures
import numpy as np
import scipy.interpolate as interpolate
from frechet import frechetDist

def rmse(px,py,tx,ty):
    pf = interpolate.interp1d(px,py,"linear")
    tf = interpolate.interp1d(tx,ty,"linear")
    n=len(tx)*5
    xc=np.linspace(px[0],px[-1],n)
    p=pf(xc)
    t=tf(xc)
    return np.sqrt(np.average(((p-t)**2)))

def nrmse(px,py,tx,ty):
    pf = interpolate.interp1d(px,py,"linear")
    tf = interpolate.interp1d(tx,ty,"linear")
    n=len(tx)*5
    xc=np.linspace(px[0],px[-1],n)
    p=pf(xc)
    t=tf(xc)
    return np.sqrt(np.average((((p-t)/p)**2)))

def dtw(px,py,tx,ty):
    p=np.array(list(zip(px,py)))
    t=np.array(list(zip(tx,ty)))
    return similaritymeasures.dtw(t,p)[0]

def frechet(px,py,tx,ty):
    n1=len(tx)
    n2=len(px)
    pn=np.array(list(zip(px,py)))[:n2//5]
    tn=np.array(list(filter(lambda x: x[0]<pn[-1][0],np.array(list(zip(tx,ty))))))
    return similaritymeasures.frechet_dist(tn,pn)

def frechet2(px,py,tx,ty):
    n1=len(tx)
    n2=len(px)
    pn=np.array(list(zip(px,py)))[:n2//5]
    tn=np.array(list(filter(lambda x: x[0]<pn[-1][0],np.array(list(zip(tx,ty))))))
    return frechetDist(tn,pn)

