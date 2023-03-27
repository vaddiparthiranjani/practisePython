# program to swap first and last element of the list
def swapList(newList):
    size=len(newList)

    # swapping
    temp = newList[0]
    newList[0]=newList[size-1]
    newList[size-1]=temp

    return newList

list1 = [23,24,21,12,12,13,78]
print(list1)
print(swapList(list1))
