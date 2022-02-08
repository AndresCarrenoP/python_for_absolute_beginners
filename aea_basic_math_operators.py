# Expressions - instructions to the computer. The simplest of them consist of values and math operators

addition = 4 + 5
print("addition", addition)

subtraction = 5 - 2
print("subtraction", subtraction)

division = 16 / 5
print("division", division)

multiplication = 3 * 8
print("multiplication", multiplication)

exponentiation = 4 ** 4
print("exponentiation", exponentiation)

floor_division = 16 // 5
print("floor_division", floor_division)

""" little trick for a ceiling division:
    using a floor division, change one of the operands to negative and multiply the whole thing * -1"""
ceiling_division = -1 * (-16 // 5)
print("ceiling_division", ceiling_division)

modulo = 7 % 3
print("modulo", modulo)
