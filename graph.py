import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
import pickle
# 300 represents number of points to make between T.min and T.max
file=open("insertion_time_gdh","rb")
data=pickle.load(file)

file.close()
x,y=data
print(x)
print(y)
# x=x[::-1]
# y=y[::-1]
xnew = np.linspace(min(x), max(x), 30) 

spl = make_interp_spline(x, y, k=3)  # type: BSpline
y_smooth = spl(xnew)

plt.plot(xnew, y_smooth)
# plt.plot(x,y)
plt.xlabel("Number of users")
plt.ylabel("Time for insertion(sec)")

file=open("insertion_time","rb")
data=pickle.load(file)

file.close()
x,y=data
xnew = np.linspace(min(x), max(x), 30) 

spl = make_interp_spline(x, y, k=3)  # type: BSpline
y_smooth = spl(xnew)

plt.plot(xnew, y_smooth)

# plt.savefig("./insertion_time_plot.png")
plt.show()