# This is the simplest way of solving the problem!
# This solves the problem by repititive addition

def add(num): # this is the function
	total = num 
	# in range(in line 5) function, "range(5)" denotes 0 to 4. 
	# So we are keeping the last number already added to total
	for i in range(num):
		total += i # adds all the numbers below num, and num is already ther (line 5)
	return total # returns the result 
	# Note:- Returned value is in integer format so we will have 
	# to convert it to string before printing along with other strings!

num = int(input("Enter the number: ")) # Taking the input and storing it in variable num
print("sum = " + str(add(num)))
