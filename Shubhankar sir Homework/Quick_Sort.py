import random

# SORTING
def Partition(lb, ub):
	key = a[lb]
	start = lb
	end = ub
	# print("Start pointer at", start, "th place", "end pointer at", end, "th place.")
	while start < end:
		while a[start] <= key:
			if start in range(0,9):
				start += 1
				# print("Start pointer at", start, "th place", "end pointer at", end, "th place.")
			else: break
		while a[end] > key:
			if end in range(0,10):
				end -= 1
				# print("Start pointer at", start, "th place", "end pointer at", end, "th place.")
			else: break
		if start < end:
			a[start], a[end] = a[end], a[start] # swap
			# print("swapped")
			# print(a)
	a[lb], a[end] = a[end], a[lb]
	# print("swapped with key")
	# print(a)
	# print("Moving to next part\n\n")
	return end
	
	
def QuickSort(lb,ub):
	if lb < ub:
		loc = Partition(lb, ub)
		if lb != 9:
			if (loc-1) in range(0,10):
				QuickSort(lb, loc-1)
			if (loc+1) in range(0,10):
				QuickSort(loc+1, ub)
				
# Making a random list of 10 one-digit numbers
a = []
for i in range(10):
	a.append(random.randint(0,9))
print("Before Sorting:-")
print(a, "\n")
QuickSort(0,9)
print("After Sorting:-")
print(a)
