# to print a dictionary where the keys are numbers between 1 and 15 (both included) and
# the values are the square of the keys.

d = dict()
for x in range(1,16):
    #if x % 2 != 0:
    d[x] = x**2


print(d)