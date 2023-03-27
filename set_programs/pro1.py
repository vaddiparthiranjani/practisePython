# create a set

set1 = set()
print(type(set1))

set2 = {1,2,3,4,4}

print(set2,"\n ", type(set2))

for i in set2:
    print(i)

# adding elements into set
set2.add(5)
print(set2)

# adding multiple elements
set2.update([6,7])
print(set2)

#removing first element
set2.pop()
print(set2)

#removing specific element
set2.discard(4)
print(set2)