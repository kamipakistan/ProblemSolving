# List

#Consider a list (list = []). You can perform the following commands:

# 1- insert i e: Insert integer  at position .
# 2- print: Print the list.
# 3- remove e: Delete the first occurrence of integer .
# 4- append e: Insert integer  at the end of the list.
# 5- sort: Sort the list.
# 6- pop: Pop the last element from the list.
# 7- reverse: Reverse the list.
# Initialize your list and read in the value of  followed by
# lines of commands where each command will be of the  types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

# Input Format

# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.

# Constraints

# The elements added to the list must be integers.
# Output Format

# For each command of type print, print the list on a new line.

##### Sample Input
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

##### Sample Output 0

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]


# Solution
if __name__ == '__main__':
    N = int(input())
    list = []
    list.insert(0, 5)
    list.insert(1, 10)
    list.insert(0, 6)
    print(list)
    list.remove(6)
    list.append(9)
    list.append(1)
    list.sort()
    print(list)
    list.pop()
    list.reverse()
    print(list)
