#Finding factors of numbers....
n = int(input("Find factors of: ")) 
backup = n
d = 2
factors = []
while d <= n :
    if n%d == 0:
        factors.append(d)
        n/=d
    else: d+=1

if len(factors)>1: print(factors)
else: print("This is a prime number.")
