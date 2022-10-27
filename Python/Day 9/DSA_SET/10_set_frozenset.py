# to make the set fixed

a=frozenset({1,2,3,4})
b=frozenset({4,5,6})
c={4,5,6}
print(a)
print(type(a))

# print(a.add(5))
#print(a.remove(4))
print(a|b)
print(a|c)