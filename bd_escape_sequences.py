"""
Escape sequences are special characters you can use in strings which allow you to do things like:
insert quotes within them
make different parts of strings appear on different lines in the output
This is NOT an exhaustive list of all of python's escape sequences,these are just some of the more commonly used ones.
"""

# TAB char represented by a \t - used to make horizontal space or indents:
print("This\tis\ta\tlot\tof\tspace.")

# new line char represented by a \n - used to insert a line break
print("line one\nline two")


# for quotes, you can use either \' or \"

# below we are escaping with \' because the string is enclosed in single quotes
print('"When I said \'immediately\', I meant today!" Said King Saul.')

# below we are escaping with \" because the string is enclosed in double quotes
print("\"Do or do not. There is no try.\"")

# \\ double backlash is used when you want to put a backlash inside a string
print("All escape sequences contain a '\\'.")
