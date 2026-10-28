name = input("Enter your name: ")

result = len(name)
print("The length of your name is:", result)

# This is a string method that returns the index of the first occurrence of a space in the name. If there is no space, it returns -1.
result = name.find("a")
print("The index of the first space in your name is:", result)

# This is a string method that returns the index of the last occurrence of a space in the name. If there is no space, it returns -1.
result = name.rfind("a")
print("The index of the last space in your name is:", result)

# This is a string method that capitalizes the first letter of the name and makes all other letters lowercase.
name = name.capitalize()
print("Your name after capitalization is:", name)

# This is a string method that converts all letters in the name to uppercase.
name = name.upper()
print("Your name in uppercase is:", name)

# This is a string method that converts all letters in the name to lowercase.
name = name.lower()
print("Your name in lowercase is:", name)

# This is a string method that checks if all characters in the name are digits. It returns True if they are, and False otherwise.
name = name.isdigit()
print("Is your name made up of digits only?", name)

name = input("Enter your name: ")

# This is a string method that checks if all characters in the name are alphabetic. It returns True if they are, and False otherwise.
name = name.isalpha()
print("Is your name made up of alphabetic characters only?", name)

phone_number = input("Enter your phone number: ")

# This is a string method that counts the number of occurrences of a specific character (in this case, a hyphen) in the phone number.
phone_number.count("-")

# This is a string method that replaces all occurrences of a specific character (in this case, a hyphen) with another character (in this case, an empty string) in the phone number.
phone_number.replace("-", "")

# This is a built-in function that provides information about the string class and its methods.
help(str)
