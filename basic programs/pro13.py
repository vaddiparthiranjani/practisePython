# program to print febonacci series

a, b = 0,1
n= int(input("enter number"))

print(a,b , end = " ")
while ( (n - 2) > 0):
    c=a+b
    print(c, end = " ")
    a,b = b,c
    n = n - 1



