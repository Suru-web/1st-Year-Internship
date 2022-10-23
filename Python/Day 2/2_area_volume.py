print("enter lenght, breadth and height values")
l=int(input("enter the length"))
b=int(input("enter the breadth"))
h=int(input("enter the height"))
while(True):
    ch=int(input("enter 1:area 2:volume 3:exit"))
    if(ch==1):
        a=l*b
        print("area of the room is: ",a)
    elif(ch==2):
        v=l*b*h
        print("volume of the room is: ",v)
    elif(ch==3):
        exit(1)      # to exit from the loop
    else:
        print("invalid choice")
#infinite loop
# exit(1) indicates successful termination

