# Python program to check if two strings are anagrams using sorted()

s1 = input("enter first string")
s2 = input("enter second string")

s1=s1.lower()
s2=s2.lower()

len1 =len(s1)
len2 =len(s2)


if len1 == len2:
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    if sorted_s1 == sorted_s2:
        print(s1," and" , s2, "are anagram ")
    else:
        print(s1,"and ",s2, " is not anagram ")
else:
    print(s1, "and ", s2, "is not anagram ")

