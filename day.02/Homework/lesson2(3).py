# Input 5 numbers and calculate  average
numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(5)]
average = sum(numbers) / 5

# Print result
print("The arithmetic mean is:", average)