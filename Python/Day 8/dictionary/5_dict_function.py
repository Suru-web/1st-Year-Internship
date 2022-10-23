# fromkeys(seq[key],value)

marks={}.fromkeys([5,4,3,2,1],100)
print(marks)

for i in marks.items():
    print(i)

print(sorted(marks))
print(sorted(marks.items()))