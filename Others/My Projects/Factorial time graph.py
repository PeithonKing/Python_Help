import time
import matplotlib.pyplot as plt

n = []
times = []

start = 1
end = 10000
interval = 100
readings = 100 # records this many amount of readings and takes the mean

for k in range(start, end, interval):
	l = 0
	for a in range(readings):
		t = time.time()
		i = 1
		f = 1
		for s in range(k):
			f *= i
			i += 1
		t = time.time() - t
		l += t
	l /= readings
	n.append(k)
	times.append(l)
	
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(n, times)
plt.show()
