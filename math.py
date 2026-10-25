import math
x = 3.14
y = 4
z = 5
q = -6

rounded_x = round(x)  # Rounds x to the nearest integer
print(rounded_x)  # Output: 3

result = abs(q)  # Returns the absolute value of y
print(result)  # Output: 6

result = pow(4, 3)  # Returns y raised to the power of z
print(result)  # Output: 64

test1 = max(x, y, z)  # Returns the maximum value among x, y, and z
print(test1)  # Output: 5

test2 = min(x, y, z)  # Returns the minimum value among x, y, and z
print(test2)  # Output: 3.14


print(math.pi)

print(math.e)

test3 = math.sqrt(x)  # Returns the square root of x
print(test3)  # Output: 1.772004514666935

test4 = math.ceil(x)  # Returns the smallest integer greater than or equal to x
print(test4)  # Output: 4

test5 = math.floor(x)  # Returns the largest integer less than or equal to x
print(test5)  # Output: 3

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
print(f"The area of the circle is: {round(area, 2)}cm²")

circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {round(circumference, 2)}cm")


a = float(input("enter side A of the triangle: "))
b = float(input("enter side B of the triangle: "))

# Using the Pythagorean theorem to calculate the length of the hypotenuse
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The length of the hypotenuse is: {round(c, 2)}")
