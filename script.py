# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize a variable to store the sum of odd numbers
sum_odd = 0

# Loop through each number in the list
for number in numbers:
    # Check if the number is odd
    if number % 2 != 0:
        # Add the odd number to the sum
        sum_odd += number

# Print the result
print("The sum of odd numbers is:", sum_odd)
