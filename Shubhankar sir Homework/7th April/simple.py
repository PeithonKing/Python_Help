def add():
	print("sum = " + str(sum(numbers)))
def avg():
	print("average = " + str(sum(numbers)/len(numbers)) + "\n")

while True:
	startnum = int(input("Enter startnum: "))
	endnum = int(input("Enter endnum: "))
	numbers = list(range(startnum, endnum+1))
	add()
	avg()
