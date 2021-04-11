p = int(input("Enter The Point Of differenciation, x= "))
def fn(x):return (2*x)
diff = (fn(p)-fn(p-(10**(-10))))*10**10
print(diff)
