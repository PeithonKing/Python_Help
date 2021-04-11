# find square root of x
xi = 6
m = 10**(-5)
det = []
if xi<0:
    x = -xi
else:
    x = xi
if x in [value**2 for value in range(0,11)]:
    for i in range(0,11):
        if x==i**2:
            if xi < 0:
                print(str(i) + "i")
            else:
                print(i)
else:
    for v in range(1,11):
        a = v**2
        b = (v-1)**2
        if x > b and x < a:
            while x < a:
                b += m
                r =(x-b**2)
                if r<=10**(-3) and r >= 0:
                    det.append(b)
            i = max(det)
            if xi < 0 :
                print(str(i) + "i")
            else:
                print(i)
