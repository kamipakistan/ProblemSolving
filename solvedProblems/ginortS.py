"""
Task:
You are given a string S.
contains alphanumeric characters only.

Your task is to sort the string S in the following manner:
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Input Format
A single line of input contains the string S.

Output Format
Output the sorted string .

Sample Input
Sorting1234

Sample Output
ginortS1324"""

# ========================================
# ============= Solution =================
# =======================================
# Enter your code here. Read input from STDIN. Print output to STDOUT
S = input()
lower = []
upper = []
oddDigits = []
evenDigits = []

for c in S:
    if c.islower():
        lower.append(c)
    elif c.isupper():
        upper.append(c)
    elif int(c) % 2==0:
        evenDigits.append(c)
    elif int(c)%2==1:
        oddDigits.append(c)
l = [lower, upper, oddDigits, evenDigits]

f = []
# sorting and adding into a specified order
for i in l:
    i.sort()
    f +=i

print("".join(f))
