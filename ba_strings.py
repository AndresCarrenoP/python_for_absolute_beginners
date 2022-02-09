ex_1 = 'this is a string.'
ex_2 = "this is also a string."
ex_3 = ""  # empty string

# In a string, each character has an index, starting with 0
ex_4 = "0123456"


# Accessing by index
ex_5 = "orange"
print(ex_5[2])
print("apple"[4])


# String slicing
# syntax = start : end
# whatever is before the : symbol is inclusive
# and whatever is after the : symbol is exclusive
ex_6 = "apricots"

print(ex_6[:3])  # from the beginning to a certain point (exclusive)
print(ex_6[2:5])  # from a starting point (inclusive) to an end point (exclusive)
print(ex_6[4:])  # from a starting point (inclusive) all the way to the end


# String concatenation
print("pecan" + " " + "pie")


# Strings that are added together can be assigned to a variable
concatenated = "R2" + "_" + "D2"
print (concatenated)
print(concatenated[3])
print(concatenated[1:4])


# String slicing does not change strings that have been assigned to variables
# Accessing characters by index does not change the string either
unchanged = "forrest gump"
sliced = unchanged[6:]
print(sliced)
print(unchanged)
print(unchanged[10])
print(unchanged)
