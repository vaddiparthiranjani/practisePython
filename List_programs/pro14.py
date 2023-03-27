# program to find the odd numbers in an array

numbers = [23,24,25,26,12,13]
count = 0
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        print(numbers[i])
        count +=1
print("count of odd numbers : ", count)



