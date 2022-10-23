print("Enter the number of elements to add to the list\n")
l2=[]
l3=[]
n=int(input())
print("Enter the list of elements")

for i in range(1,n+1):
    l1=int(input())
    l2.append(l1)
print("The list is :",l2)
for i in l2:
    if(i%2==0):
        l3.append(i)
print("The even numbers in the list are :",l3)