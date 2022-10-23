def add():
    sum = a + b
    print("Sum is : ", sum)


def sub():
    s = a - b;
    print("Subtraction is : ", s)


def div():
    d = a / b
    print("Div is : ", d)


def mul():
    m = a * b
    print("Multiplication is : ", m)

while(True):
    print("Enter 2 numbers : ")
    a=int(input())
    b=int(input())
    print("Enter your choice :\n"
          "1 : Add\n"
          "2 : Sub\n"
          "3 : Div\n"
          "4 : Multi\n")
    choice = int(input())



    if(choice==1):
        add()
    elif(choice==2):
        sub()
    elif(choice==3):
        div()
    elif(choice==4):
        mul()
    else:
        print("Invalid choice input")