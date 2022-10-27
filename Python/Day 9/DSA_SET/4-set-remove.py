s1={10,20,50}
s1.remove(10)
print(s1)
#s1.remove(1)       #Gives error if element not found
print(s1)

s2={1,2,3,4,5,6,7,8}
s2.discard(1)
print(s2)
s2.discard(100)   #Does not give error if element is not found
print(s2)

#pop
s2.pop()
print(s2)

#clear
s2.clear()
print(s2)