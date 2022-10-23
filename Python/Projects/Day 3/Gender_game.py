gender = input("What is your Gender? (M or F) :\t")
first_name = input("What is your First Name?\t")
last_name = input("What is your Last Name?\t")
age = int(input("Enter your age :\t"))
if (gender == "F"):
    if (age >= 20):
        mar = input("Are you married ? (y or n) ")
        if (mar == "y"):
            print("Then i shall call you Mrs.", first_name, last_name)
        else:
            print("Then i shall call u Ms.", first_name, last_name)
    else:
        print("Then i shall call u ", first_name, last_name)

elif (gender == "M"):
    if (age >= 20):
        print("Then i shall call you Mr.",first_name,last_name)
    else:
        print("Then i shall call u ",first_name,last_name)

