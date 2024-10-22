#1
# or operator:
# The result will be True if at least one of the operands is True.
# It will be False only if both operands are False.

# and operator:
# The result will be True only if both operands are True.
# It will be False if at least one operand is False.


#2
#  or operator results

print("or operator results:")
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

# and operator results

print("and operator results:")
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

#3
my_name = "Barbare"
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: ")) 
result = user_age >= 18 and user_name == my_name
print(result)