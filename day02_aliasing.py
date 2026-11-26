import numpy as np
import matplotlib.pyplot as plt

#define array
fs = 100
t = np.arange(0, 10, 1/fs)

#inputs
frequency = 5
A = 1


#calculating y
y =   A * np.sin ( 2 * np.pi * frequency * t )

#plotting
plt. plot(t , y)
plt. xlabel("t (s)")
plt. ylabel ("y (m)")
plt. plot( t , y, "o-")
plt.xlim(0, 1)
print(len(t))
plt. show()