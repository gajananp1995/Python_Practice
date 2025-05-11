import math

# Asking the user for input
num = float(input("Enter a number: "))

# Calculating square root, natural logarithm, and sine (in radians)
square_root = math.sqrt(num)
natural_log = math.log(num) if num > 0 else "Undefined (logarithm of non-positive numbers)"
sine_value = math.sin(num)

# Displaying the results
print(f"Square root : {square_root}")
print(f"logarithm  : {natural_log}")
print(f"Sine : {sine_value}")
