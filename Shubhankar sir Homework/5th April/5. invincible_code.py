def add(num):
	i = num
	for j in range(num):
		i += j
	return i
while True:
	while True:
		try:
			num = int(input("Enter the number: "))
			break
		except:
			print("Invalid Input!")
			continue
			
	print("sum = " + str(add(num)) + "\n")
