# program to check whether the given integer is a prime number or not

num = int (input("Enter the number"))

isprime = 1

for i in range(2, num//2):
    if num % i == 0:
        isprime = 0
        break

if isprime == 1:
    print("Number is prime")
else:
    print("Number is not prime")


