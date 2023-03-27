# to extract a list of values from a given list of dictionaries.

def test(list1, marks):
    result = [d[marks] for d in list1 if marks in d]
    return result

marks = [{"math":90,"science": 90},
         {"math":89,"science":90},
         {"math":67,"science":78}
         ]

print("original Dictionary")
print(marks)

subject = "math"
print("for maths :", test(marks,subject))
