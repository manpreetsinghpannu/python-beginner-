# conditional expression = a concise way to evaluate a condition and return one of two values based on whether the condition is true or false.
# It is often referred to as a ternary operator in programming.
# X if condition else Y


num = 5

# This is a conditional expression
print("Positive" if num > 0 else "negative")

num = 6
result = "Even" if num % 2 == 0 else "Odd"  # This is a conditional expression
print(result)

num = 5
a = 6
b = 7
max_num = a if a > b else b  # This is a conditional expression
min_num = a if a < b else b  # This is a conditional expression
print("The maximum number is:", max_num)
print("The minimum number is:", min_num)

age = 25
status = "Adult" if age >= 18 else "Minor"  # This is a conditional expression
print("The person is an:", status)

temp = 30
# This is a conditional expression
weather = "Hot" if temp > 30 else "Warm" if temp > 20 else "Cold"
print("The weather is:", weather)

user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print("The user has:", access_level)
