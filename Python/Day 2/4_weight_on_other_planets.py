w=float(input("please enter your current earth weight"))
print("I have information for the following planets \n 1:venus 2:mars 3:jupiter 4:saturn 5:uranus 6:neptune 7:exit")
while(True):
    ch = int(input("which planet are you visiting ?"))
    if(ch==1):
            pw=w*0.78
            print("your weight would be ",pw," pounds on that planet")
    elif(ch==2):
            pw=w*0.39
            print("your weight would be ",pw," pounds on that planet")
    elif(ch==3):
            pw=w*2.65
            print("your weight would be ",pw," pounds on that planet")
    elif(ch==4):
            pw=w*1.17
            print("your weight would be ",pw," pounds on that planet")
    elif(ch==5):
            pw=w*1.05
            print("your weight would be ",pw," pounds on that planet")
    elif(ch==6):
            pw=w*1.23
            print("your weight would be ",pw," pounds on that planet")
    elif(ch==7):
            exit(1)
    else:
            print("invalid choice")


