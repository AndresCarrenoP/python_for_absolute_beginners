# print() can be used to print directly the value of variables
example_1 = 3.14159
example_2 = 24601
example_3 = True

print(example_1)
print(example_2)
print(example_3)


# you can also print values typed directly inside the parenthesis
print(2019)


# you can also use print to display the result of an expression assigned to a variable
example_5 = 10 + 9
print(example_5)

# you can also use print to display the result of an expression typed directly inside the parenthesis
print((4 + 5) * 3)

# to break a single print into multiple lines, use '\n'
print("line one\nline two")

# to print a blank line, use (''), or (""), or () nothing at all inside the parentheses
print('')
print("")
print()
print("line six because lines 3, 4 and 5 are blank")

# to print without separating by lines, you can use end=""
#   this overrides the print() function, more info here:
#   https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/
print()
print("*** examples of no line break: ***")
print("string_one", end=", ")
print("string_two", end=", ")
print("string_three", end=", ")
print("string_four")
