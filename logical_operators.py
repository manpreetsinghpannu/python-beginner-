# logical operators = evaluate multiple expressions and return a boolean value ( or, and, not )
# or = at least one expression is true
# and = all expressions are true
# not = negates the boolean value of an expression

temp = 25
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor conditions are not suitable for a picnic.")
else:
    print("The outdoor conditions are suitable for a picnic.")

temp = 22
is_sunny = False

if temp >= 22 and is_sunny:
    print("The outdoor conditions are suitable for a picnic.")
    print("it is a sunny day")
elif temp <= 0 and is_sunny:
    print("The outdoor conditions are not suitable for a picnic.")
    print("it is a sunny day")
elif 28 > temp > 0 and is_sunny:
    print("The outdoor conditions are suitable but warm.")
    print("it is a sunny day")
elif temp <= 0 and not is_sunny:
    print("The outdoor conditions are not suitable for a picnic.")
    print("it is not a sunny day")
elif 28 > temp > 0 and not is_sunny:
    print("The outdoor conditions are suitable but warm.")
    print("it is not a sunny day")
