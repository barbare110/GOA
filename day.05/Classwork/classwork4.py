#1
# enter users age
age = int(input("Enter your age: "))

# how many times 10 fits into the age
count = age // 10

# Print the result
print(f"10 fits into your age {count} times.")
#2

age_str = input("Enter your age: ")
print(type(age_str))  # first type
age_float = float(age_str)
print(type(age_float))  # secondd new type


#3
name = input("Enter your name: ")
number = int(input("Enter a number: "))
result = name * number
print(result)

#4
# Implicit Type Conversion: Automatically done by Python adding int and float.
# examples: 
x = 5 + 3.2  # x = float (result: 8.2)

# Explicit Type Conversion: Manually done using functions int(), float().
# example:
a = "10"
b = int(a) 
 # b is integer now (10)


# same code without f print --> after class just in case
age = int(input("Enter your age: "))
count = age // 10
print("10 fits into your age {} times.".format(count))

age_str = input("Enter your age: ")
print(type(age_str))  
age_float = float(age_str)
print(type(age_float)) 

name = input("Enter your name: ")
number = int(input("Enter a number: "))
result = name * number
print(result)
x = 5 + 3.2  
a = "10"
b = int(a) 