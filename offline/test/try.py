# test
from load_file import load_file

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate

arr = load_file("./stream-1/stream-1.yaml")
print(arr)
x,y = map(np.array,zip(*arr))
x = list(map(lambda x:x.timestamp(), x))
x = np.array(x)
t = x[0]
x = x-t
a = interpolate.interp1d(x,y,kind='previous',fill_value=(0,y[-1]), bounds_error=False)
x1 = np.linspace(x[0], x[-1], 100)
y1 = a(x1)
print(x)
print(y)
# plt.plot(x,y,'o')
# plt.plot(x1,y1)
# plt.plot(x,y)
uti = (a(x1)-a(x1-1.0))/1.0
plt.plot(x1,uti)
plt.plot(x1,y1)
# plt.plot(x1,y1)
plt.show()
