# main_script.py
from math_operations import add, subtract, multiply, divide

# Example usage
num1 = 10
num2 = 5

# Addition
result_add = add(num1, num2)
print(f"Addition: {num1} + {num2} = {result_add}")

# Subtraction
result_subtract = subtract(num1, num2)
print(f"Subtraction: {num1} - {num2} = {result_subtract}")

# Multiplication
result_multiply = multiply(num1, num2)
print(f"Multiplication: {num1} * {num2} = {result_multiply}")

# Division
try:
    result_divide = divide(num1, num2)
    print(f"Division: {num1} / {num2} = {result_divide}")
except ValueError as e:
    print(f"Error: {e}")
