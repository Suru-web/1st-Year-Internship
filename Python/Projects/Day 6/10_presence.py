l=[]
count=0
num=int(input("Enter the number of elements you want to add to the list\t"))
print("Enter the elements\n")
for i in range(1,num+1):
    l1=int(input())
    l.append(l1)
print("The list is :",l)
key=int(input("Enter the element you want to search\t\t"))
for i in l:
    if(i==key):
        count=count+1
if(count>0):
    print("The key is present ",count," time\s in the list")
else:
    print("Key is not present")