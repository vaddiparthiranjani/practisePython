# function that accepts a string and counts the number of upper and lower case letters

def string_test(s):
    lower_count=0
    upper_count =0
    for i in s:
        if i.islower():
            lower_count +=1
        elif i.isupper():
            upper_count+=1
        else:
            pass
    print("No of upper case letters : ",upper_count)
    print("No  of lower case letters : ",lower_count)
    return

string_test("This is a PYTHON code")