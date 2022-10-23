# arithmetic operations: +,-,*,/
a=int(input("enter a value"))
b=int(input("enter b value"))
ch=int(input("enter ur choice 1:Add 2:Sub 3:Mul 4:Div"))
if(ch==1):
    res=a+b
    print("addition of {0} and {1} is {2}".format(a,b,res))
elif(ch==2):
    res = a-b
    print("subtraction of {0} and {1} is {2}".format(a, b, res))
elif (ch == 3):
    res = a*b
    print("product of {0} and {1} is {2}".format(a, b, res))
elif (ch == 2):
    res = a/b
    print("division of {0} and {1} is {2}".format(a, b, res))
else:
    print("invalid choice")