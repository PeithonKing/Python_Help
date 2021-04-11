n = int(input("Enter the number: "))
fibonacci = [1,1]
for i in range(0,n-2):
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
for i in fibonacci:
	print(i)
print( "\nThe sum of this seriese upto " + str(n) + " terms is " + str(sum(fibonacci)) + "." )
