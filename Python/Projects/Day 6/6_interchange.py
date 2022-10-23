l=[]
global num, temp
num=int(input("Enter the number of elements you want to add to the list\t"))
print("Enter the elements\n")
for i in range(1,num+1):
    l1=int(input())
    l.append(l1)
print("The list is :",l)
def swap():
    temp=l[0]
    l[0]=l[num-1]
    l[num-1]=temp
    return l
swap()
print("The values after interchanging is :",l)