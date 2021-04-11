def add(num):
	total = num 
	for i in range(num):
		total += i
	return total

while True:
	num = int(input("Enter the number: "))
	print("sum = " + str(add(num)) + "\n")
