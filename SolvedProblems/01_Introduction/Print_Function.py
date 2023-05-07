# ============ Task ==============
# The included code stub will read an integer, n, from STDIN.
# Without using any string methods, try to print the following:
# 123...n
# Note that "..." represents the consecutive values in between.

# ========= Solution ========
# Checking if the code is being run as the main program
if __name__ == '__main__':
    # Getting input from user and converting it to an integer
    n = int(input())

    # Looping through the range of 1 to n+1,
    # and printing each number without a newline character
    for i in range(1, n + 1):
        print(i, end="")
