# to check whether a given key already exists in a dictionary.

dict = {1 : "Raj", 2 : "pop", 3 : "sam",5:"kiran",6:"Mani",7:"lata"}

def is_key_present(x):
    if x in dict:
        print("key is present")
    else:
        print("key is not present")
    return

is_key_present(3)
is_key_present(4)

# to access the elements using loops

for dic_key , dic_value in dict.items():
    print(dic_key, "->" , dic_value)