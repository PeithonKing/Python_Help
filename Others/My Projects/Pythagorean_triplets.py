# We will prompt for a number, and will find the set of all pythagorean triplets less than that!
n = int(input("Enter a number: "))
# We define an empty list which will be used to get the total number of results found.
length = []
i = 0
# The line below needs a little bit of calculations which I dont feel like telling u!
# Just know for now that I have found out that I dont need to see the cases where i > that....
while i <= n-n/1.414+1:
    # increase i each time this is run....
    i += 1
    # j stars from 0 which also gets increased at line 14 
    j = 0
    while j < n:
        j += 1
        k = j+i
        p = (k**2-j**2)**0.5
        # Now we have to find the cases where p is an integer, and eleminate the rest.
        if p < j and p%1 == 0 and k <= n:
            # we print it in the desired way!
            print(str(int(p)) + ", " + str(j) + ", " + str(k))
            # we find the number of results by adding the value in the list "length",
            #  and we will calculate its length later.... in line 24
            length.append(j)
print("Total " + str(len(length)) + " triplets found!")
