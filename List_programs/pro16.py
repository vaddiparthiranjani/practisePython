# program to insert a number to any position in a list

lst1 = [1,2,3,4]

x = int(input("enter the position"))
y = int(input("enter the number"))

print("original list ", lst1)

lst1.insert(x,y)

print("new list ", lst1)

# delete number from a list

lst1.pop(x)

print("new list after deletion ", lst1)