print("Enter the number of elements to add to the list\n")
l2=[]
n=int(input())
print("Enter the list of elements")

for i in range(1,n+1):
    l1=int(input())
    l2.append(l1)
print("The list is :",l2)
print("Enter the number of elements to add to the list which is to be subtracted from the main list\n")
m=int(input())
print("Enter the list of elements")
l4=[]
for i in range(1,m+1):
    l3=int(input())
    l4.append(l3)
print("The list to be subtracted is :",l4)
l=[x for x in l2 if x not in l4]
print(l)