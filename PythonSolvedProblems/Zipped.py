"""
Task

The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.

The format for the general mark sheet is:

Student ID → ___1_____2_____3_____4_____5__               
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86  
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5 
Input Format

The first line contains N and X separated by a space.
The next X lines contains the space separated marks obtained by students in a particular subject.

Output Format

Print the averages of all students on separate lines.

The averages must be correct up to  decimal place.
"""
# =====================================================
# ================== Solution ========================
# =====================================================
# N students, X subjects.
N, X = map(int, input().split())

# list of student marks lists
marks = [list(map(float, input().split())) for _ in range(X)]

# zipping 
for m in list(zip(*marks)):
    print(sum(m)/len(m))
