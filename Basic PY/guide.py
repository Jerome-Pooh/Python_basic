'''string = ["Jerome" , 1 , 2 , "True"]
print(string[3])'''

# Sets
'''
set1 = {"Roger", "Syd"}
set2 = {"Roger"}

intersect = set1 & set2

print(intersect)

x = 1

students_count = 1000  # variable
rating = 4.99  # float
is_published = False  # boolean
course_name = "Python Programming"  # string
print(students_count)
'''
# Strings
# course = "Python Programming"
# Functions
'''
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:-3])
print(course[:])
'''

# Escape Sequences
# course = "Python \"Programming"
# course = "Python \nProgramming"
# print(course)

# Formatted Strings
'''
first = "John"
last = "Smith"
full = f"{len(first)} {last}"
print(full)
'''
# String Methods
'''
course = "   Python Programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("Pro"))
print(course.replace("P", "-"))
print("Pro" in course)
print("swift" not in course)
'''

# Numbers
'''
x = 10
x = 1.1
x = 1 + 2j
print(x)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
'''
# https://docs.python.org/3/library/math.html
'''
import math
print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.9))

# Type Conversion
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")
print(y)
'''
# int(x)
# float(x)
# bool(x)
# str(x)

# conditional statements
'''
temperature = 35
if temperature > 30:
    print("It's a hot day")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's not a hot day")
'''
# Ternary Operator
'''
age = 17
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
'''
# Logical Operators
# and = need both conditions to be true
# or = need one condition to be true
# not = reverse the condition
'''
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
'''
# Chaining Comparison Operators
# age should be between 18 and 65
# age = 22
# if age >= 18 and age < 65:
# if 18 <= age < 65:
#   print("Eligible")


# For Loops
# for number in range(1, 10, 2):
# print("Attempt", number, (number) * ".")


# For Else
'''
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
'''

# Nested Loops
for x in range(1, 5):
    for y in range(1, 3):
        print(f"({x}, {y})")

# Iterables
# for x in "Python":
# print(x)

# While Loops
number = 100
while number > 0:
    print(number)
    number //= 2
