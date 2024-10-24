# My last name
my_last_name = "Williams" # random last name

# Prompt the user for their age and last name
user_age = int(input("Enter your age: "))
user_last_name = input("Enter your last name: ")

# Check if age is 18 or older or if last name matches
result = user_age >= 18 or user_last_name == my_last_name

# Print the result
print(result)  # Outputs True if age is 18 or older, or if last name matches