# Initialize an empty list
numbers = []

# Input 6 numbers from the user
for i in range(6):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Find the maximum and minimum values using built-in functions
maximum = max(numbers)
minimum = min(numbers)

# Print the results
print("Maximum value is:", maximum)
print("Minimum value is:", minimum)
