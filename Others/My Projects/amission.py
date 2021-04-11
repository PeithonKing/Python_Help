usernames = []
registered_users = {}
while True:
    n = input("\nWhat is your name? ")
    name = n.lower()
    if name in usernames:
        print("Welcome " + name.title())
        ph_no = input("Enter your phone number: ")
        registered_users[name] = ph_no
        usernames.remove(name)
        print("Registration Complete!")
        print("Thank you!")
    elif name in registered_users.keys():
        print("You have already been admitted!")
    elif name == 'quit':
        if len(usernames) != 0:
            print("We have more users to be registered!")
            p = input("Do you really want to end registration? (yes/no) ")
            if p.lower() == "yes":
                break
            if p.lower() == "no":
                continue
        else:
            break
    else:
        print("Invalid username!")
        print("Are you a new user?")
        while True:
            p = input("Do you want me to jot down your name? (yes/no) ")
            if p.lower() == "yes":
                usernames.append(name)
                print("Your name has been added,login again to register.")
                print("Thank You!")
                break
            elif p.lower() == "no":
                print("Thank you!")
                break
            else:
                print("Could not understand!! Sorry!!")
                continue
print("\nProcess of registration completed successfully! \nThe list of phone numbers of the registered users is: ")
for name, phone in registered_users.items():
    print(name.title() + ": " + phone)
input("\nPress enter to quit.")
