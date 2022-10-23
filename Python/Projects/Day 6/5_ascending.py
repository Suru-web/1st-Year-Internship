l=[]
print("Enter the number of elements in the list\n")
num=int(input())
print("Enter the elements in the list\n")
for i in range(1,num+1):
    l1=int(input())
    l.append(l1)
print(l)
for i in range(0,num-1):
    if(l[i]<l[i+1]):
        k=1
    else:
        k=0
        break
if(k==1):
    print("In ascending order")
else:
    print("Not in ascending order")