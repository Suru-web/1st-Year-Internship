choice=0
dis=0
des='destination'
def dest(choice):
    if(choice==1):
        des='Rajajinagar'
        return des
    elif(choice==2):
        des ='Hebbal'
        return des
    elif(choice==3):
        des = 'Vijay Nagar'
        return des
    elif(choice==4):
        des = 'Yeshwantpur'
        return des
    else:
        print("Invalid destination\n")
        return -1

def dist(choice):
    if(choice==1):
        dis=15
        return dis
    elif(choice==2):
        dis =10
        return dis
    elif(choice==3):
        dis = 20
        return dis
    elif(choice==4):
        dis = 25
        return dis
    else:
        print("Invalid destination\n")
        return -1




print("Welcome to Yalahanka Station\n")
print("\nYou are at Yalahanka\n")
print("Where do you wanna go?\n")
print("\t 1) Rajajinagar\n"
      "\t 2) Hebbal\n"
      "\t 3) Vijay Nagar\n"
      "\t 4) Yeshwantpur\n")
choice=int(input())
dis=dist(choice)
des=dest(choice)
print("Source : Yalahanka\n")
print("Destination :",des)
print("Distance : ",dis)

