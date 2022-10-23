# 3 functions to add elements into a list : append(), insert(), extend() ---> all 3 functions in 1 file only

#Append()
l1=[]
print(l1)
l1.append(20)
print(l1)
l1.append("Hello")
l1.append(30)
print(l1)

l2=[]
for i in range(1,10):
    l2.append(i)
    print(l2)

#adding one list to another list
l3=[10,"hi"]
l3.append(l2)
print(l3)



#Using insert() function
i1=[100,200,300,400]
i1.insert(1,150)  #---> insert(pos,element) = it adds the element to the index number provided, that is 150 to 1st index pos
print(i1)


#Using extend() dunction
e1=[1,2]
e1.extend([3,4,5,6,"Hello"])  #  ---> adds elements to the list in the last
print(e1)