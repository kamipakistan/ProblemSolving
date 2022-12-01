# There is an array of n integers. There are also 2 disjoint sets,A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i E A, you add 1 to your happiness. If i E B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

# Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

# Input Format

# The first line contains integers  and  separated by a space.
# The second line contains  integers, the elements of the array.
# The third and fourth lines contain  integers,  and , respectively.

# Output Format

# Output a single integer, your total happiness.

# Sample Input

# 3 2
# 1 5 3
# 3 1
# 5 7
# Sample Output

# 1

# Explanation
# You gain 1 unit of happiness forelements 3 and 1 in set A. You lose 1 unit for 5 in set B. The element 7 in set B does not exist in the array so it is not included in the calculation.

# Hence, the total happiness is 2-1=1.


# ======== Solution ==========
# Enter your code here. Read input from STDIN. Print output to 
STDIN = map(int, input().split())
array_ = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for i in array_:
    if i in A:
        happiness+=1
    elif i in B:
        happiness-=1
print(happiness)
