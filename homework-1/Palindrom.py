# Ask the user to enter a number
number = input("Enter a number:")

# Reverse the entered number 
reversedNumber = number[::-1]

# Check if the reversed number is the same as the original number
if number == reversedNumber:
    print("This number is a palindrome")
else:
    print("This number is not a palindrome")    
