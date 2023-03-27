# String is pallindrom or not

text = input("enter string :")

if text == text[::-1] :
    print("String is pallindrom")
else:
    print("String is not pallindrom")

# String is Symmetrical or not

half = int(len(text)/2)

first_half = text[:half]
second_half = text[half:]

if first_half == second_half :
    print("String is Symmetrical")
else:
    print("String is not Symmetrical")


