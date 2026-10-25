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

temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("The outdoor conditions are suitable for a picnic.")
    print("it is a sunny day")
