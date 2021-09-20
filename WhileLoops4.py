Loop = False

while Loop == False:
    choice = input("Type yes to enter the program or no to keep asking:")

    if choice == "yes":
        print("You have entered the program")
        Loop = True

    else:
        print("You have chosen to loop the program")
print("The loop has finished")
