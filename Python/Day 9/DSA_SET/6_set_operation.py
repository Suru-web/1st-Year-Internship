# set union method

a={1,2,3,4,5}
b={4,5,6,7,8}

# use | operator

print("union of set")
print(a|b)
print(a.union(b))
print(b.union(a))

print("intersection of sets")
print(a&b)
print(b&a)
print(a.intersection(b))
print(b.intersection(a))

print("difference of sets")
print(a-b)
print(b-a)

print("symmetric difference")
print(a^b)
print(b^a)

