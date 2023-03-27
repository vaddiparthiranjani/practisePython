# program to swap two elements in a list at given position

def swapPositions(list, pos1,pos2):
    list[pos1], list[pos2] =list[pos2],list[pos1]
    return list

List=[2,3,4,5,6]

pos1, pos2 = 3,5

print(swapPositions(List,pos1-1,pos2-1))


