name = input("Enter your name: ")
age = int(input("Enter your age: "))
# Output: Hello <name>! (where <name> is the user input)

# use f string when adding variables to a string

age = age + 1

print(f"Hello {name}!")
print("Happy Birthday!")  # Output: Happy Birthday!
# Output: You are <age> years old. (where <age> is the user input)
print(f"You are {age} years old.")


# exercise -- calculate the area of a rectangle
lenght = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = lenght * width
print(f"The area of the rectangle is: {area} cm^2")

# erercise 2 Shopping cart program

item = input("Enter the item you want to buy: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))

total = price * quantity
# the /s is used to indicate plural form of the item
print(f"you have purchased {quantity} {item}/s")
# the (s) is used to indicate plural form of the item
print(f"you have purchased {quantity} {item} (s)")

# Output: The total is: $<total> (formatted to 2 decimal places)
print(f"The total is: ${total:.2f}")
# Output: The total is: $<total> (not formatted to 2 decimal places)
print(f"The total is: ${total}")
