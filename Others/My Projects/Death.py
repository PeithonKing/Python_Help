name=input("What is your Name?")
print("We would ask you for your email address.\nJust wait and watch what happens at the end!    ;)")

while True:
	email=input("Enter your valid email address: ")
	if "@gmail.com" not in email and "@niser.ac.in" not in email:
		print("Invalid Email Address!")
		continue
	rt = input("Are you sure?(y/n) ")
	if "y" in rt:
		break
	elif "n" in rt:
		continue
	else:
		print("Pardon!!")

print("We are gonna ask your AGE and tell you when you will die!")
while True:
	yrs=input("How old are you?(in years) ")
	try:
		age=int(yrs)
	except ValueError:
		print("This should be an integer, your age!")
		continue
	if age in range(17,25):
		break
	else:
		print("Do you really think you can lie to me !!  Huh !!")
		continue
print("\nWe would ask you 10 simple questions!\nAre you ready?")
input('When you are ready and press "ENTER"')

n=age

q1=("How much exercise do you do in a typical day?", "1) Do not exercise", "2) < 30 mins", "3) > 30 mins", "4) > 1 hour")
q1=("How often do you drink alcoholic beaverages?", "1) Do not drink", "2) rarely", "3) occasionally", "4) hour")
q1=("Do you have dysmenorrhea? If yes,how often?", "1) Never", "2) Rarely", "3) Occasionally", "4) Always")


Questions=("q1","q2","q3")
