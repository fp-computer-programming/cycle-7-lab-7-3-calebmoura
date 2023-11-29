# Author: Caleb Moura

def greeting():
    """
    This function prints "Hello World" on one line because it is its only command.
    """
    print("Hello World!")

    # Return the docstring for the greeting function.
    return greeting.__doc__

# Call greeting function.
greeting()

# Function to add two numbers.
def add_numbers(a, b):
    """
    Add two numbers and return the result.
    """
    return a + b

# Function to subtract two numbers.
def subtract_numbers(a, b):
    """
    Subtract b from a and return the result.
    """
    return a - b

# Main code
if __name__ == "__main__":
    # Test the functions
    result_add = add_numbers(5, 3)
    result_subtract = subtract_numbers(10, 4)

    # Print the results.
    print(f"Addition Result: {result_add}")
    print(f"Subtraction Result: {result_subtract}")

# Test Case 1
# Adding two positive numbers.
test_result_1 = add_numbers(8, 2)
print(f"Test Case 1 - Addition Result: {test_result_1}")

# Test Case 2
# Subtracting a negative number from a positive number.
test_result_2 = subtract_numbers(15, -5)
print(f"Test Case 2 - Subtraction Result: {test_result_2}")

# Test Case 3
# Adding two negative numbers.
test_result_3 = add_numbers(-3, -7)
print(f"Test Case 3 - Addition Result: {test_result_3}")

# Test Case 4
# Subtracting a positive number from a negative number.
test_result_4 = subtract_numbers(-10, 2)
print(f"Test Case 4 - Subtraction Result: {test_result_4}")