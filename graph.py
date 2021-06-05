import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from scipy.interpolate import interp1d, InterpolatedUnivariateSpline
from scipy import arange, array, exp
import pickle
# 300 represents number of points to make between T.min and T.max



file=open("insertion_time_gdh","rb")
data=pickle.load(file)

file.close()
x,y=data

extrap = 2500

xnew = np.linspace(min(x), max(x), 30) 
# y_smooth = f(xnew)
spl = make_interp_spline(x, y, k=1)  # type: BSpline
y_smooth = spl(xnew)
xnewnew = np.linspace(min(x), max(x)+extrap, 30) 
f = InterpolatedUnivariateSpline(xnew,y_smooth,k=1)
plt.plot(xnewnew,f(xnewnew),label="GDH")
# plt.plot(x,y)
plt.xlabel("Number of users")
plt.ylabel("Time for insertion(sec)")

file=open("insertion_time","rb")
data=pickle.load(file)

file.close()
x,y=data
lastx = x[-1]
lasty = y[-1]

x += [i for i in range(lastx+5, lastx+extrap,5)]
y+= [lasty for i in range(extrap//5 - 1)]
xnew = np.linspace(min(x), max(x), 300) 

spl = make_interp_spline(x, y, k=3)  # type: BSpline
y_smooth = spl(xnew)

plt.plot(xnew, y_smooth,label="TGDH")
plt.legend()
plt.savefig("./insertion_time_plot.png")

plt.show()








file=open("insertion_time_gdh","rb")
data=pickle.load(file)

file.close()
x,y=data

extrap = 2500

xnew = np.linspace(min(x), max(x), 30) 
# y_smooth = f(xnew)
spl = make_interp_spline(x, y, k=1)  # type: BSpline
y_smooth = spl(xnew)
xnewnew = np.linspace(min(x), max(x)+extrap, 15) 
f = InterpolatedUnivariateSpline(xnew,y_smooth,k=1)
plt.plot(xnewnew,f(xnewnew),label="GDH")
# plt.plot(x,y)
plt.xlabel("Number of users")
plt.ylabel("Time for insertion(sec)")

file=open("deletion_time","rb")
data=pickle.load(file)

file.close()
x,y=data
x=x[::-1]
y=y[::-1]
lastx = x[-1]
lasty = y[-1]
print(x)
x += [i for i in range(lastx+5, lastx+extrap,5)]
y+= [lasty for i in range(extrap//5 - 1)]
xnew = np.linspace(min(x), max(x), 300) 
print(x)
spl = make_interp_spline(x, y, k=3)  # type: BSpline
y_smooth = spl(xnew)

plt.plot(xnew, y_smooth,label="TGDH")
plt.legend()
plt.savefig("./deletion_time_plot.png")

plt.show()