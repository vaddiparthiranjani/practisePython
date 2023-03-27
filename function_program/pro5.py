# to filter a list of integers using Lambda.

nums=[1,2,3,4,5,6,7,8]

print("list of numbers : ", nums)

even_nums =list(filter(lambda x: x% 2 ==0 , nums))
print("list of even numbers", even_nums)

odd_nums =list(filter(lambda x : x%2 != 0,nums))
print("list of odd numbers", odd_nums)

# to get square and cubes of integers in list using lambda

squares = list(map(lambda x: x**2,nums))
print("squares of numbers in the list : ", squares)

cubes = list(map(lambda x : x**3,  nums))
print("CUBES of numbers in the list : ", cubes)
