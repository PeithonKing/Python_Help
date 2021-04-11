# This code makes use of formulas
# The runtime of the previous code (simple.py) depended
# on the input value, how large it was.... but this code takes 
# the same amount of time for all inputs!

def add(num):
	num = num*(num+1)/2
	return num
num = int(input("Enter the number: "))
print("sum = " + str(add(num))) 
# Instead you can use line 12 to get rid of the decimal digits
# You can use a int() before add(num) like below
# print("sum = " + str(int(add(num)))) 
