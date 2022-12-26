"""
# =====================================================================================================
# ======================================== Day 6: Let's Review ========================================
# =====================================================================================================

Task
Given a string, S, of length N that is indexed from 0 to N-1,
print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Example
s = adbecf

Print abc def

Input Format
The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a string, S.

Output Format
For each String Sj(where 0<=j <=T-1), print Sj's even-indexed characters,
followed by a space, followed by Sj's odd-indexed characters.

Sample Input
2
Hacker
Rank

Sample Output
Hce akr
Rn ak

"""

# ==================================== Solution =============================
# The first line contains an integer, T (the number of test cases).
T = int(input())

# Each line i of the T subsequent lines contain a string, S.
for i in range(T):
    s = input()
    even = [s[i] for i in range(len(s)) if i%2==0 or i == 0]
    odd = [s[i] for i in range(len(s)) if i%2==1]
    print("".join(even), "".join(odd))
    
    
