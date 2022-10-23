def acc_creation():
    global bal
    global name
    name=input("Enter your name\n")
    global accnum
    accnum=int(input("Enter account number\n"))
    bal=int(input("Enter the initial bank balance\n"))
def deposite():
    global bal
    dep=int(input("Enter the amount to deposite\n"))
    bal=bal+dep
    print("Total amount : ",bal)
def withdraw():
    global bal
    withd=int(input("Enter the amount to withdraw\n"))
    if(bal<withd):
        print("Can not withdraw as balance is less that the withdraw amount\n")
    else:
        bal=bal-withd
        print("Remaining balance : ",bal)
def display_user():
    print("Your name :\t",name)
    print("Your account number : ",accnum)
    print("Your available balance : ",bal)
print("Welcome to SBI Internet Banking\n")
acc_creation()

while(True):
    ch=int(input("Enter your choice : 1) Deposite 2)Withdraw 3)Display User\n"))
    if(ch==1):
        deposite()
    elif(ch==2):
        withdraw()
    elif(ch==3):
        display_user()
    elif(ch==4):
        exit(1)
    else:
        print("Invalid choice")
