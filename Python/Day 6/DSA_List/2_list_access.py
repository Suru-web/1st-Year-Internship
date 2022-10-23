#   0 1 2 3 4    ---> Positive Indexing
#  -5-4-3-2-1    ---> Negative Indexing
l1=[1,2,3,4,5,6,7,8,9,10,11,12,13]
print(l1[3])     # -----> prints element with 3rd index, i.e it prints element 4
print(l1[-3])    # -----> prints element with -3 negative index (3)

#slicing
print(l1[:3])    # -----> prints only 1st 3 elements
print(l1[1:3])
print(l1[2:])    # -----> from 2nd index to last index