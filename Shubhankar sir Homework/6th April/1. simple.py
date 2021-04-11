def add(startnum, endnum):
	total = endnum
	for i in range(startnum, endnum):
		total += i
	return total

while True:
	startnum = int(input("Enter startnum: "))
	endnum = int(input("Enter endnum: "))
	print("sum = " + str(add(startnum, endnum)) + "\n")
