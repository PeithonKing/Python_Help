import random

letters = [chr(x) for x in range(ord('a'), ord('z') + 1)] 
numbers = [str(x) for x in range(0,10)]

password = ''

for i in range(6):
	s=random.choice(letters)
	password = password + s

for i in range(2):
	n=random.choice(numbers)
	password = password + n

for i in range(2):
	x=random.choice(letters)
	password = password + x.upper()

print(password)
