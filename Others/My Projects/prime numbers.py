def find_primes(start,end):
    if start < 2:
        start += 2
    primes = []
    for i in range(start,end+1):
        d = 2
        lsit = []
        while d < i**.5:
            if i%d == 0 :
                lsit.append(d)
                d+=1
            else: d+=1
        if len(lsit) == 0: primes.append(i)
    print (primes)
    print(len(primes))
    
find_primes(0,2000)
