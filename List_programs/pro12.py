# program to display the sum of n numbers using a list

numbers = []

num = int(input("Enter the number"))

for i in range(num):
    x = int(input("Enter number"))
    numbers.append(x)


print("sum of numbers in 5a list ", sum(numbers))
