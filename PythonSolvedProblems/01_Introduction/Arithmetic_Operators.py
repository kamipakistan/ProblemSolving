
# =============== Task =================
# The provided code stub reads two integers from STDIN, a and b.
# Add code to print three lines where:
# 1. The first line contains the sum of the two numbers.
# 2. The second line contains the difference of the two numbers (first - second).
# 3. The third line contains the product of the two numbers.


# ============= Solution ===================

# Checking if the code is being run as the main program
if __name__ == '__main__':
    # Getting input from user and converting to integer for variable a
    a = int(input())
    # Getting input from user and converting to integer for variable b
    b = int(input())

    # Adding and printing a and b
    print(a + b)
    # Subtracting and printing b from a
    print(a - b)
    # Multiplying and printing a and b
    print(a * b)
