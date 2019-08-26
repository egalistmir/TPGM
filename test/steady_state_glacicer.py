import numpy as np
import matplotlib.pyplot as plt

rho = 900 #km m-3 ice density
g = 9.8 #m s-2 gravity
tau = 100 #kPa driving stress
#zELA = 600 # m difference between headwall elevation and ELA

s = np.arange(0.05, 0.21, 0.01) #slope, noting that the slope gradient is constant
fig = plt.figure(figsize = (11,7), dpi = 100)

for i in range(1,10):
	zELA = i * 100 
	L = (2 / s) * (tau / (rho * g * s) + zELA)
	plt.plot(s, L / 1000)
	#plt.legend()
plt.savefig('test8026.png')



