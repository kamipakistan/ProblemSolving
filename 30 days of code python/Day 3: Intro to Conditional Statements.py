"""
# =====================================================================
# ============ Day 3: Intro to Conditional Statements =================
# =====================================================================
Task
Given an integer, N, perform the following conditional actions:

If N is odd, print Weird
If N is even and in the inclusive range of 2 to 5, print Not Weird
If N is even and in the inclusive range of 6 to 20, print Weird
If N is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

Input Format
A single line containing a positive integer, .

Output Format
Print Weird if the number is weird; otherwise, print Not Weird.
"""

# ============================== Solution ===================================
if __name__ == '__main__':
    N = int(input().strip())
    # If N is odd, print Weird
    if N % 2 == 1:
        print("Weird")
    # If N is even 
    elif N % 2 == 0:
        # If N is even and in the inclusive range of 2 to 5, print Not Weird
        if 1 < N < 6:
            print("Not Weird")
        # If N is even and in the inclusive range of 6 to 20, print Weird
        elif 5 < N < 21:
            print("Weird")
        # if N is even and greater than 20, print "Not Weird"
        elif N >20:
            print("Not Weird")
            
