"""
Task:
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
Input Format
A single line containing the space separated values of N and M.

Output Format
Output the design pattern.
"""

# ======================= Solution ===================================
N, M = map(int, input().split())
mid = (N+1)//2
string = ".|."
counter = 1
for i in range(1, N+1):
    if i < mid:
        print((string*counter).center(M, "-"))
        counter+=2
    elif i == mid:
        print("WELCOME".center(M, "-"))
        counter-=2
    else:
        print((string*counter).center(M, "-"))
        counter-=2
        
