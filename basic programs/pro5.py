# Reverse Words in a string

#input String

text = "this is Python code"

s = text.split()[::-1]

l = []

for i in s:
    l.append(i)

print(text)
print(" ".join(l))
