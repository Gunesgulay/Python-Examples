# Get the current salary and raise percentage from the user
salary = float(input("Enter the current salary: "))
raise_percentage = float(input("Enter the raise percentage (%): "))

# Calculate the raise percentage as a decimal
raise_percentage = raise_percentage / 100

# Calculate the updated salary
updated_salary = salary + (salary * raise_percentage)

# Display the result
print(f"Updated salary: {updated_salary:.3f}")
