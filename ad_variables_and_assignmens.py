"""
Unlike Java where you need to declare the variable type like: int num1 = 25;
Or Javascript where you declare variables with var or let like: var num1 = 25;
In python you simply put the variable name and its value
"""
ex_int1 = 1
ex_float1 = 2.27
ex_bool1 = True
print(ex_int1, ex_float1, ex_bool1)

# you can directly reassign the value of a variable in Python like this:
ex_int1 = 4
print("After reassign: ", ex_int1, ex_float1, ex_bool1)

# to declare a variable without a value in Python, you use 'None', as 'None' is the uninitialised value in Python
ex_int2 = None
print(ex_int2)
