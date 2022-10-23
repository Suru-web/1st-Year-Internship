# 2 funtions to remove elements -> remove() and pop()

#remove()
l1=[3,1,2,3,4,5]
print(l1)
l1.remove(3)  #----> removes the first occurance of the element '3' in the list
print(l1)

#pop()
l2=[1,2,3,4,5]
print(l2)
l2.pop()     #----> removes last element from the list
print(l2)
l2.pop(1)    #----> pops specific index element
print(l2)