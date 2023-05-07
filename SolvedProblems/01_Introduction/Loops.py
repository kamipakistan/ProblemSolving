
# ===================== Task ===================
# The provided code stub reads and integer, n , from STDIN.
# For all non-negative integers i<n, print i**2.

# ================== Solution ==================

# Checking if the code is being run as the main program
if __name__ == '__main__':
    # Getting input from user and converting it to an integer
    n = int(input())

    # Checking if n is non-negative
    if n >= 0:
        # Looping through the range of n, and printing the square of each number
        for i in range(n):
            print(i ** 2)
    else:
        # If n is negative, printing an error message
        print("Error: input must be non-negative")
