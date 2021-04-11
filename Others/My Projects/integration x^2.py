a = 2
b = 5
m = 10**5
ys = []
for value in range(a*m,b*m):
    y = ((value/m)**2)/m
    ys.append(y)
int = sum(ys)
print("The integration of x^2 from " + str(a) + " to " + str(b) + " is, " + str(int))
