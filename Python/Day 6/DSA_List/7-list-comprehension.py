l1=[]
for i in range(1,10):
    l1.append(i*i*i)
    print(l1)

#similarly, we can do it like this also
l2=[i*i for i in range(1,10)]
print(l2)

l3=[i ** 3 for i in range(1,10) if(i%2==0)]
print(l3)

print(len(l1))