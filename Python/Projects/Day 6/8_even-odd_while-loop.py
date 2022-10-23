l=[]
even,odd,x,y=0,0,0,0
num=int(input("Enter the number of elements you want to add to the list\t"))
print("Enter the elements\n")
for i in range(1,num+1):
    l1=int(input())
    l.append(l1)
print("The list is :",l)
i=0
while(i<num):
    if(l[i]%2==0):
        even=even+1
    else:
        odd=odd+1
    i=i+1

print("Number of even elements in the list is ",even)
print("Number of odd elements in the list is ",odd)