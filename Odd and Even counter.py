# A program to check for odd and even numbers
# The program terminates when zero is entered

# Variable declared
odd_numbers = 0
even_numbers = 0

# Read the first number
number = int(input("Enter a number or type 0 to stop: "))
while number != 0:
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1
    # Read the second number
    number = int(input("Enter a number or type 0 to stop: "))

# Print results
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

# Exit the program
input("Press enter key to exit program...")

