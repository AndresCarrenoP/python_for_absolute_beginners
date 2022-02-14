"""
Similar to how the string function allows you to change a number to a string,
the int() and float() functions allow you to turn strings into numbers.
"""

# int() function
user_int = input("Please enter an integer.")
print("User integer is:", user_int)
print("User integer type is:", type(user_int), " because it was NOT converted")

print()
user_int2 = int(input("Please enter another integer."))
print("User second integer is:", user_int2)
print("User second integer type is:", type(user_int2), " because it WAS converted")

print()
# float() function
user_float = input("Please enter a float.")
print("User float is:", user_float)
print("User float type is:", type(user_float), " because it was NOT converted")

print()
user_float2 = float(input("Please enter another float."))
print("User second float is:", user_float2)
print("User second float type is:", type(user_float2), " because it WAS converted")
