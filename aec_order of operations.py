# operator precedence in python
# () parenthesis has the highest precedence, it will be done first
# ** exponentiation comes second
# % modulus, / division, // floor division and * multiplication come third
# + plus and - minus come last


expression = (9 - 7) * 2 ** 3 + 10 % 6 // -1 * 2 - 1
# Step 1 is operations inside the parenthesis:
#   2 * 2 ** 3 + 10 % 6 // -1 * 2 - 1

# Step 2 is exponentiations:
#   2 * 8 + 10 % 6 // -1 * 2 - 1

# Step 3: since multiplication, modulus and floor division
# all have the same level of precedence, they are done next, from left to right:
#   16 + 10 % 6 // -1 * 2 - 1
#   16 + 4 // -1 * 2 - 1
#   16 + -4 * 2 - 1
#   16 + -8 - 1

# Step 4 since addition and subtraction have the same level of precedence,
# they are done next, from left to right:
# 16 + -8 - 1
# 8 - 1

# Result is 7

print("given expression: (9 - 7) * 2 ** 3 + 10 % 6 // -1 * 2 - 1")
print("the result of the expression above is:", expression)
