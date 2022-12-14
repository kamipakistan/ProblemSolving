# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.

# Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

# Example
# Set ([1, 2, 3]) is a strict superset of set([1, 3]).
# Set ([1, 2, 3]) is not a strict superset of set ([1, 2, 3]).
# Set ([1, 2, 3]) is not a strict superset of set ([1, 3, 5]).

# Input Format

# The first line contains the space separated elements of set A.
# The second line contains integer n, the number of other sets.
# The next  lines contains the space separated elements of the other sets.


# Output Format

# Print True if set A is a strict superset of all other N sets. Otherwise, print False.

# Sample Input 0

# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12
# Sample Output 0

# False
# Explanation 0

# Set A is the strict superset of the set([1, 2, 3, 4, 5]) but not of the ([100, 11, 12])set because 100 is not in set A.
# Hence, the output is False.

# ========================================================================
# ============================= Solution =================================
# ========================================================================
# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
N  = int(input())

result = set()
for _ in range(N):
    s = set(map(int, input().split()))
    result.add(A.issuperset(s))

if len(result)> 1:
    print("False")
else:
    print("True")
