from scipy.interpolate import interp1d
import numpy as np
   
def packet_uniform(x,y,k=100):
    k1 = len(x)//k
    return x[::k1],y[::k1]

def byte_uniform(x,y,k=100):
    a = interp1d(x,y,kind='previous')
    x1 = np.linspace(x[0],x[-1],k)
    y1 = a(x1)
    return x1,y1

def gradient_based(x,y,k=100):
    a = interp1d(x,y,kind='previous')
    
    xc = x
    yc = y

    gr = np.gradient(yc,xc)
    gri = zip(gr,xc)

    _,x1 = zip(*list(sorted(gri,reverse=True))[:k])
    x1=sorted(x1)
    y1 = a(x1)
    return x1,y1

def arc_length_linear(x,y,k=100):
    a = interp1d(x,y,kind='linear')
    calen = 0
    cp = x[0],y[0]
    alen=[] # length parameter
    for i,j in zip(x,y):
        calen+=np.sqrt((cp[0]-i)**2 + (cp[1]-j)**2)
        alen.append(calen)
        cp=i,j
    
    arc = zip(x,alen)
    arc_sample = np.linspace(0,calen,k) # uniform arc sampling

    arc_inv = interp1d(alen,x,'linear')

    x1 = arc_inv(arc_sample)
    y1 = a(x1)
    return x1,y1

def arc_length_spline(x,y,k=100):
    a = CubicSpline(x,y)
    calen = 0
    cp = x[0],y[0]
    alen=[] # length parameter
    for i,j in zip(x,y):
        calen+=np.sqrt((cp[0]-i)**2 + (cp[1]-j)**2)
        alen.append(calen)
        cp=i,j
    
    arc = zip(x,alen)
    arc_sample = np.linspace(0,calen,k) # uniform arc sampling

    arc_inv = interp1d(alen,x,'linear')

    x1 = arc_inv(arc_sample)
    y1 = a(x1)
    return x1,y1