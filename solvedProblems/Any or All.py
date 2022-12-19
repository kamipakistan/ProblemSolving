"""
Task

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

Input Format

The first line contains an integer N. N is the total number of integers in the list.
The second line contains the space separated list of N integers.

Constraints


Output Format

Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

Sample Input

5
12 9 61 5 14 
Sample Output

True"""

# ============================================================
# ===================== Solution ============================
# ===========================================================
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
NsList = input().split()
positive = all(True if int(i) > 0 else False for i in NsList)
palindrom = any(True for i in NsList if i[::-1] == i)
print(positive and palindrom)
