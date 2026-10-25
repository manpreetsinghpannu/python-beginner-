age = int(input("Please enter your age: "))

if age >= 100:
    print("You are too old to create an account.")
elif age < 0:
    print("Invalid age. Please enter a valid age.")
elif age >= 18:
    print("You are eligible to create an account.")
else:
    print("You are not eligible to account.")

response = input("Do you want to continue? (Y/N): ")

if response == "Y":
    print("You chose to continue.")
elif response == "N":
    print("You chose not to continue.")

name = input("Please enter your name: ")

if name == "":
    print("You did not enter a name.")
else:
    print(f"Hello, {name}")


for_sale = True

if for_sale:
    print("The item is for sale.")
else:
    print("The item is not for sale.")
