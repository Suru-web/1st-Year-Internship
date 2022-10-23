def factorial():
    fact =1
    num=int(input("Enter a number\t\t"))
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of ",num," is ",fact)

factorial()