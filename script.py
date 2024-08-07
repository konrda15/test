# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize a variable to store the sum of even numbers
sum_even = 0

# Loop through each number in the list
for number in numbers:
    # Check if the number is even
    if number % 2 == 0:
        # Add the even number to the sum
        sum_even += number

# Print the result
print("The sum of even numbers is:", sum_even)
