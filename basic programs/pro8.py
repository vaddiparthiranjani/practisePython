# Sum of Digits in a number

x = int(input("Enter the number"))

sum = 0

while (x > 0):
    sum =sum + x % 10
    x = int(x/10)

print("Sum of digits : ",sum)