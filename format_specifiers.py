# format specifiers = {value :flags} format a value based on what flags are inserted.

# .(number) f = round a float to a specific number of decimal places (fixed point notation)
# :(number) = allocate a number with spaces to a specific width
# :03 = allocate a number with spaces to a specific width and fill with leading zeros
# :< = left align a value within a specific width
# :> = right align a value within a specific width
# :^ = center align a value within a specific width
# :+ = show a sign for positive numbers
# := = show a sign for positive numbers and place the sign to the left of the number
# : = show a sign for positive numbers and place the sign to the right of the number
# , = show a comma as a thousands separator

price_1 = 3.14159
price_2 = -987.65
price_3 = 12.34

print(f"Price 1: {price_1:.2f}")
print(f"Price 2: {price_2:.2f}")
print(f"Price 3: {price_3:.2f}")
