# ============== Task ==================
# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines.
# The first line should contain the result of integer division,  a// b.
# The second line should contain the result of float division,  a/b .
# No rounding or formatting is necessary.

# ============ Solution ===============

# Checking if the code is being run as the main program
if __name__ == '__main__':
    # Getting input from user and converting to integer for variable a
    a = int(input())
    # Getting input from user and converting to integer for variable b
    b = int(input())

    # Performing integer division on a and b, and printing the result
    print(a // b)
    # Dividing a by b, and printing the result as a float
    print(a / b)
