"""
sources: https://www.pythonpool.com/python-semicolon/
https://www.flake8rules.com/rules/E702.html

In python, we don’t use semicolons, but it is not restricted.
Python does not use a semicolon to denote the end of the line.
The use of semicolon is to write the multiple statements on the same line.
"""

# Splitting statements with the help of semicolons
# first we will have 3 statements, each on its own line
print("Hy")
print("Python")
print("Pool")

print()

# Or, we can get the same result by writing the 3 statements in the same line and separating them with semicolons
# HOWEVER keep in mind that this is considered an anti-pattern
print("Hy"); print("Python"); print("Pool")

print()

# If for some lazy reason we want to have everything on a single line, we rather do this:
print("Hy\nPython\nPool")
