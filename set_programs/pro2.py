# intersection of two sets

s1={1,2,3,4}
s2={3,4,5,6}
s={2,3}
print("set 1 :-",s1)

print("set2 : ",s2)
#intersection
s3 = s1 & s2
print("Intersection of s1 and s2 : ",s3)

#union
s4=s1.union(s2)
print("union of s1 and s2",s4)
#difference
s5=s1.difference(s2)
print("difference of s1 and s2 :", s5)
s5 = s2.difference(s1)
print("difference of s2 and s1 :", s5)

# asymmetric difference

s5=s1.symmetric_difference(s2)
print("symmetric difference of s1 and s2 :", s5)

# subset of set

print(" s is subset of s1", s.issubset(s1))
print("s is subset of s2 :", s.issubset(s2))