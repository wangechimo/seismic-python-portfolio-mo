import numpy as np
import matplotlib.pyplot as plt

#define array
t = np.arange(0, 10, 0.01)
#inputs
frequency = 5
A = 1

#calculating y
y =   A * np.sin ( 2 * np.pi * frequency * t )

#plotting
plt . plot(t , y)
plt. xlabel("t (s)")
plt . ylabel ("y (m)")
plt. show()