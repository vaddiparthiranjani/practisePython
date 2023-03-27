# Combine two lists into a dictionary

def test(key, value):
    return(dict(zip(key,value)))

l1= [1,2,3,4]
l2 = [1,4,9,16]

print(l1)
print(l2)

print(test(l1,l2))
