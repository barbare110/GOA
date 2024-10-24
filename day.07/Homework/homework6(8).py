# Get 5 numbers from the user
numbers = []
for i in range(5):
    num = float(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)

# Calculate the arithmetic mean
mean = sum(numbers) / len(numbers)

# Get the first and last number
first_number = numbers[0] #number[0] retrieves the very first number entered.
last_number = numbers[-1] #number[-1] retrieves the very last number entered.

# Calculate the product of the first and last number
product = first_number * last_number

# Check if the mean is less than the product
if mean < product:
    result = "The arithmetic mean is less than the product of the first and last numbers."
else:
    result = "The arithmetic mean is not less than the product of the first and last numbers."

# Output the results
print("Arithmetic Mean:", mean)
print("Product of First and Last Numbers:", product) #The product of the first and last number is calculated by multiplying those two numbers together.
print(result)