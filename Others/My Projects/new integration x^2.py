# integrating f(x) = x^2 with "while"
print("We are going to find the integration of x^2")
a = int(input ("enter lower limit "))
b = int(input ("enter upper limit "))
c = a
m = 10**(-5)
inte = 0
if b>=a:
    while b>=a :
        a+=m
        inte+=(a**2)*m
    print("The required integration of x^2 from " + str(c) + " to " + str(b) + " is " + str(inte) + ".")
else:
    print("Upper limit must be larger than lower limit")
