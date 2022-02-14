# Personal note: functions are similar to methods, sort of.

"""
There are at least five parts to every function:
• The key word 'def'
• The function name (it follows the same naming rules and conventions as variable names)
• Parentheses
• A colon
• Then code that the function is meant to run
    this code needs to be indented 4 spaces to let Python know that the code is associated with the function
"""


# 'def' is the keyword to define a function
def prints_five_lines_below():
    print("this")
    print("is")
    print("an")
    print("example")
    print()


# Now we can call this function over and over
# to call a function, type its name followed  by ()
prints_five_lines_below()
prints_five_lines_below()
prints_five_lines_below()
prints_five_lines_below()


# Functions can also have parameters within the () as in Java
# the parameter name follows the same naming rules and conventions as variable names
def function_name(parameter_name):
    print(parameter_name + 2)


# now, to call the function we pass the argument
function_name(58)
print()


# we can also add as many parameters as we want


def function_name2(p1, p2, p3):
    print(p1 + str(p2) + p3)


first_str = "The number "

function_name2(first_str, 5, " is an integer")
print()


"""
When you create a function, you can give default values to its parameters,
in the event that the function is called without arguments for those parameters.
"""


def default_values(num1=7, num2=8):
    print("result of multiplying " + str(num1) + " * " + str(num2) + " is", num1 * num2)


# calling the function without arguments will use the default values
default_values()

"""
calling the function only with one argument,
it will use that one as the 1st one
and for the other one it will use the default value
"""
default_values(2)

# calling the function with all its arguments
default_values(4, 6)
print()


"""
'return' works the same way as in Java:
Often, you will want your function to produce something that can be used in expressions
or assigned to a variable rather than just printed,
the 'return' keyword is what will allow you to do that.
"""


def default_values2(num1=7, num2=8):
    return num1 * num2


print(str(default_values2()) + " + 44 = ", default_values2() + 44)

print("Or the same as above, but with arguments:")
print(str(default_values2(12, 15)) + " + 44 = ", default_values2(12, 15) + 44)
