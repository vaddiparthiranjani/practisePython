# program to print even length words in a string

# input string

x = "This a Python Code"

s = x.split()

for i in s:
    if len( i) % 2 == 0:
        print(i)


