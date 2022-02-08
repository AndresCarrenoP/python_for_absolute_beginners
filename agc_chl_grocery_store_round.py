"""
A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:
Penne 16 oz Pack of 12 - $16.68
Arrabiata Pasta Sauce 24 oz - $6.98
Bag of 20 Organic Garlic Cloves - $16.78
Italian Seasoning 1.5 oz Bottle - $15.26
Artisan Baguettes Twin Pack - $3.00
12 oz Bag of Meatballs - $4.39

In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression.
The subtotal is just the sum of all of their prices.
Use print() to display the result of the expression.
"""

penne = 16.68
arrabiata = 6.98
garlic_cloves = 16.78
italian_seasoning = 15.26
artisan_baguettes = 3.00
meatballs = 4.39
subtotal = round((penne + arrabiata + garlic_cloves + italian_seasoning + artisan_baguettes + meatballs), 2)

print("solved with round():", subtotal)
