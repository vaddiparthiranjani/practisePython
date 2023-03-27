# program to find the largest number in a list

list1 = [23,34,33,13,24,44,11]

big = list1[0]

for i in range(len(list1)):
    if ( list1[i] > big):
        big = list1[i]
        position = i


print("List of numbers :", list1)
print("Largest Number from the List :", big, " At position : ", position)