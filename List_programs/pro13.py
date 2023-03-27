# program to implement linear search

numbers = [2,3,4,5,6,1,9]

f = 0
x= int(input("Enter value to search : "))
for i in range(len(numbers)) :
    if x == numbers[i] :
        print("Sucessful search element is at position : ",i)
        f = 1
        break
if f == 0:
    print("unsucessful search ")
