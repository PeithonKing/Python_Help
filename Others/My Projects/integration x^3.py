import math

def f(x):
	return (1-math.cos(x))
	
lower_limit = 0
upper_limit = 2*math.pi
# lower_limit = int(input("Input lower limit: "))
# upper_limit = int(input("Input upper limit: "))
m = 10**4

ys = []
for value in range(int(lower_limit*m), int(upper_limit*m)):
    y = (f(value/m))/m
    ys.append(y)
inte = sum(ys)
print("The integration of f(x) from " + str(lower_limit) + " to " + str(upper_limit) + " is, " + '{:.10f}'.format(inte))
