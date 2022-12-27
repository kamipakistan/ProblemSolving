"""
# =========================================================================================================
# ============================================== Day 7: Arrays ============================================
# =========================================================================================================

Task
Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

Example
A = [1, 2, 3, 4]

Print 4 3 2 1. Each integer is separated by one space.

Input Format
The first line contains an integer,  (the size of our array).
The second line contains  space-separated integers that describe array 's elements

Sample Input
4
1 4 3 2

Sample Output
2 3 4 1
"""

# =============================== Solution ==========================
if __name__ == '__main__':
    
    # The first line contains an integer, N (the size of our array).
    n = int(input().strip())
    
    # The second line contains N space-separated integers that describe array A's elements.
    arr = list(map(int, input().rstrip().split()))
    print(*arr[::-1])
