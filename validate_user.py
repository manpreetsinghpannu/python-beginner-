# validate user input exercise
# username is no more than 12 characters long
# usernmame must not contain any spaces
# username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Error: Username must be no more than 12 characters.")
elif not username.find(" ") == -1:
    print("Error: Username must not contain any spaces.")
elif not username.isalpha():
    print("Error: Username must not contain digits.")
else:
    print(f"welcome, {username}")
