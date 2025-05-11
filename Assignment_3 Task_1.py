def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Calling the function and printing the output
num = 5  # Sample number
print(f"Factorial of {num} (using loop) is: {factorial_iterative(num)}")
