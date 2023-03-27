# Basic operations on dict


dict = {1 : "Raj", 2 : "pop", 3 : "sam"}
dict1 = {5:"kiran",6:"Mani",7:"lata"}
dict2 = { }
print(dict)

# add new element in dict

dict.update({4:"Ram"})
print(dict)

# concatenate the dicts into one

print(dict)
print(dict1)

for d in (dict,dict1) : dict2.update(d)

print(dict2)
