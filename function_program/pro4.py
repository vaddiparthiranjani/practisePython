# lambda functions

r= lambda x: x+2
print(r(4))

x=lambda x,y :x*y
print(x(3,4))

# sorting list of a  using lambda

sub_marks =[("English", 89),("Hindi", 78), ("Maths", 88)]

print(sub_marks)

sub_marks.sort(key = lambda x:x[1])

print(sub_marks)
