# add an item to tuple


tup = (2,3,4,5,6)

print(tup)

tup = tup +(3,)

print(tup)

# to count the number of times specified element occurs in the tuple
print(tup.count(3))

# to get the index of the specified number
print(tup.index(3))

# to find the specified element exists int he tuple

print(2 in tup)

# slicing of the tuple

print(tup[:3])
print(tup[0:4])
print(tup[3:])
print(tup[::-1])

#length of tuple

print(len(tup))
