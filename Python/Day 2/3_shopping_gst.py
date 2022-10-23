print("welcome to online shopping")
sum=0
gst=0
while(True):
    ch=int(input("enter the product number 1:laptop 2:mobile 3:earphones 4:speakers 5:exit"))
    if(ch==1):
        sum=sum+20000
        print("the laptop is added to the cart")
    elif(ch==2):
        sum=sum+15000
        print("the mobile is added to the cart")
    elif(ch==3):
        sum=sum+5000
        print("the earphones are added to the cart")
    elif(ch==4):
        sum=sum+5500
        print("the speakers are added to the cart")
    elif(ch==5):
        break
    else:
        print("invalid choice")
print("thanks for shopping")
print("the subtotal is : ",sum)
gst=sum+sum*0.18
print("the total amount including gst is : ",gst)

