# program to find the factorial of a number using recursion
def fact(n):
    if n==1:
        f=1
    else:
        f = n * fact(n-1)
    return f

num = int(input("Enter the number"))

result = fact(num)

print("Factorial is :",result)