# Approximation errors occur when using decimal numbers (floats) in python

# the expression below should print 4.03, however it prints 4.029999999999999
ex_1 = 1.23 + 2.80
print(ex_1)

"""
The reason is that Python is built on top of the C language,
and C language approximates float's using a fixed number of binary digits
and some numbers cannot be represented with exactness by the limited number of binary digits
"""

# There are two work-arounds:

# 1) Avoid using floats altogether and use integers instead, and then divide them
ex_2 = (123 + 280) / 100
print(ex_2)


# 2) use round() function, but it's only useful if:
#   you know the number of digits that are supposed to show after the decimal point, or
#   you only want an approximation, and only want a certain number of digits displayed after the decimal point
# Syntax: round(expression that you want to use it on, number of decimal places that you want to round to)
ex_3 = 1.23 + 2.80
print(round(ex_3, 2))
