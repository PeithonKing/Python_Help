# using the builtin sum() function

def add(startnum, endnum):
	print("sum = " + str(sum(list(range(startnum, endnum+1)))) + "\n")
startnum = int(input("Enter startnum: "))
endnum = int(input("Enter endnum: "))
add(startnum, endnum)
