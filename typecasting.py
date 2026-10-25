name = "Manny"
age = 27
gpa = 3.7
is_student = True

# typecasting

print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>
print(type(gpa))   # Output: <class 'float'>
print(type(is_student))  # Output: <class 'bool'>

print(int(gpa))  # Output: 3
print(float(age))  # Output: 27.0

name = bool(name)  # Convert name to boolean
print(name)  # Output: True (non-empty string evaluates to True)
