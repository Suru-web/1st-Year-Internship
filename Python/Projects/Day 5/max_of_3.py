def max():
    global a,b,c
    if(a>b and a>c):
        print(a," is greater")
    elif(c>a and c>b):
        print(c, " is greater")
    elif(a<b and b>c):
        print(b,' is greater')

print("Enter 3 numbers\n")
a=int(input())
b=int(input())
c=int(input())
max()

