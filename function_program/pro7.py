# to sort a given list of lists by length and value using lambda.

def sorted_sub_lists(input_list):
    result = sorted(input_list,key = lambda l : (len(l),l))
    return  result

original_list = [[2],[0,1],[1,2,3],[2,3],[0]]

print("original list :",original_list)

print("sorted list by length ", sorted_sub_lists(original_list))