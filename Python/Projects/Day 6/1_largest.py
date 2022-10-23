print("Enter the number of elements to add to the list\n")
l2=[]
n=int(input())
print("Enter the list of elements")

for i in range(1,n+1):
    l1=int(input())
    l2.append(l1)
print(l2)
big=l2[0]
for i in l2:
    if(i>big):
        big=i
print(big)