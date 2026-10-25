weight = float(input("Enter the weight"))
unit = input("Enter the unit Kilogarm or Pounds (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"The converted weight is: {round(weight, 2)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"The converted weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} is an invalid unit")
