n=50
#n = int(input("Enter a number: "))
length = 0
i = 0
while i <= n*0.293+1:
    i += 1
    j = 0
    while j < n:
        j += 1
        k = j+i
        p = (k**2-j**2)**0.5
        if p < j and p%1 == 0 and k <= n:
            print(str(int(p)) + ", " + str(j) + ", " + str(k))
            length+=1
print("\nTotal " + str(length) + " triplets found below " + str(n) + "!")
