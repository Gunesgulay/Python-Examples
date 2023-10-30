import math

# Ask the user to input radius
radius = float(input("Enter the radius of the circle:"))

# Calculate the area of the circle
area = math.pi * radius**2

# Calculate the circumference of the circle
circumference = 2 * math.pi * radius

# Display the results
print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")