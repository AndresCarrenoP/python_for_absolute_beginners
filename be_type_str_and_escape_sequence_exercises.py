"""
Create a variable and assign it a float
Use print() and type() to print the data type of the variable in the output
Use str() on the variable from step 1 and concatenate it with the string " is a float." then use print() to display the result
print() the string "Hello, I'm [name], it's nice to meet you!" including quotes (you will need to use the \' or \" escape sequence depending on whether you enclose your strings in single quotes or double quotes.)
"""

ex_1 = 1.127
print(type(ex_1))
ex_2 = str(ex_1) + " is a float."
print(ex_2)
print("\"Hello, I'm [name], it's nice to meet you!\"")  # escaping with \"
print('\'Hello, I\'m [name], it\'s nice to meet you!\'')  # escaping with \'
