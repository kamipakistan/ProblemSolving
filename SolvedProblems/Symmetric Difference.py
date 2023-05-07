# Task
# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# Input Format

# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.

# Output Format

# Output the symmetric difference integers in ascending order, one per line.

# Sample Input

# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}
# Sample Output

# 5
# 9
# 11
# 12

# ============== Solution =============== #
# Enter your code here. Read input from STDIN. Print output to STDOUT
M = input()
set_1 = set(map(int, input().split()))
N = input()
set_2 = set(map(int, input().split()))

symmetric_difference = set_1.difference(set_2).union(set_2.difference(set_1))


sortedList = sorted(list(symmetric_difference))
for i in sortedList:
    print(i)

