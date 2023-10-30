# Ask the user to input their height and weight
height = float(input("Enter your height in meters:"))
weight = float(input("Enter your weight in kilograms:"))

# Calculate the body mass index
bodyMassIndex = weight / (height * height)

# Display the result
print("Body Mass Index:", bodyMassIndex)
