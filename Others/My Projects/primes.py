# Finding all prime umbers les than "n"
n = int(input("I will find all the prime nubers less than the number you enter :"))
primes = []
for i in range(2,n):
    d = 2
    lsit = []
    while d < i:
        if i%d == 0 :
            lsit.append(d)
            d+=1
        else: d+=1
    if len(lsit) == 0: print str(i)
