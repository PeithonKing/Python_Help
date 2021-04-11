a = 1
b = 2
m = 10**5
ys = []
for value in range(a*m,b*m):
    y = ((value/m)**3)/m
    ys.append(y)
int = sum(ys)
print("The integration of x^3 from " + str(a) + " to " + str(b) + " is, " + str(int))
