"""
Create a variable and assign it the string "Just do it!"
Access the "!" from the variable by index and print() it
Print the slice "do" from the variable
Get and print the slice "it!" from the variable
Print the slice "Just" from the variable
Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.
"""

ex_1 = "Just do it!"
print(ex_1[10])  # !
print(ex_1[5:7])  # do
ex_2 = ex_1[8:]  # it!
print(ex_2)
print(ex_1[:4])  # Just
ex_3 = "Don't " + ex_1[5:]  # Don't do it!
print(ex_3)
