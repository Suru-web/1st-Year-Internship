l=[]
num=int(input("Enter the number of elements you want to add to the list\t"))
print("Enter the elements\n")
for i in range(1,num+1):
    l1=int(input())
    l.append(l1)
print("The list is :",l)
l2=[x for x in l if x>0]
print("The list of positive elements in the list is :",l2)