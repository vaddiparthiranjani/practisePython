# find maximum of three numbers

def maximum(x,y,z):
    if x>y and x>z :
        return x
    elif y > z:
        return y
    else:
        return z


a,b,c = 14,25,36
print(maximum(a,b,c))
