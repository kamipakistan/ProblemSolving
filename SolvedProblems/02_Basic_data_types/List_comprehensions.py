# ================= TASK ===============

# You are given three integers x, y
# and z representing the dimensions of a cuboid along with an integer n.
# Print a list of all possible coordinates given by (i, j, k) on a 3D grid
# where the sum of i+j+k is not equal to n.

# ================= Solution ===========

if __name__ == '__main__':
    # Get four integer inputs from the user and store them in separate variables
    x = int(input())  # Input the value of x
    y = int(input())  # Input the value of y
    z = int(input())  # Input the value of z
    n = int(input())  # Input the value of n

    # Generate a list of lists that contains all possible combinations of i, j, and k
    # where i is between 0 and x, j is between 0 and y, and k is between 0 and z,
    # but only if the sum of i, j, and k is not equal to n
    l = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]

    # Print the resulting list to the console
    print(l)
