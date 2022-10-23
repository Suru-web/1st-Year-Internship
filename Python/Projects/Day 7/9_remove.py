t=(10,20,30,40,50,60)
t1=[]
a,b,c,d,e,f=t
print("The giver tuple is :",t)
num=int(input("Enter a number to remove from the tuple\n"))
for x in t:
    if(x!=num):
      t1.append(x)
print(tuple(t1))