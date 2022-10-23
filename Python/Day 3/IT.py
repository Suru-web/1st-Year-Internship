while(True):
    salary=int(input("Enter your salary\n"))
    if(salary<=50000):
        print("No tax applicable")
    elif(salary>50000 and salary<=60000):
        tax=(salary-50000)*0.1
        print("Tax of",tax,"needs to be payed")
    elif(salary>60000 and salary<=150000):
        tax=(salary-50000)*0.2
        print("Tax of", tax, "needs to be payed")
    else:
        tax=(salary-50000)*0.3
        print("Tax of", tax, "needs to be payed")
