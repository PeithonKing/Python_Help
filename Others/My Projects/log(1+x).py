x = 2
parts = []
for n in range(1,3):
    p = ((-1)**(n-1))*(x**n)/n
    parts.append(p)
    print(sum(parts))
