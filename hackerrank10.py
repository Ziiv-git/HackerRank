'''
Objective
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!
Task
Given a base-10 integer, n, convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
Input Format
A single integer,n.
Constraints
1<n<10**6
Output Format
Print a single base-2 integer denoting the maximum number of consecutive 1's in the binary representation of n .
Sample Input 1
5
Sample Output 1
1
Sample Input 2
13
Sample Output 2
2
Explanation
Sample Case 1:
The binary representation of 5 is 101 , so the maximum number of consecutive 1's is 1 .
Sample Case 2:
The binary representation of 13 is 1101, so the maximum number of consecutive 1's is2 .'''

n = int(input('Enter the no:'))
temp = 0
s = ''
rem = 0
while n>0:
    temp = int(n/2)
    rem = n%2
    s = s+str(rem)
    n = temp

print(s)
#for finding consecutive 1's in binary representatino
length = 0
count = 0
for i in range(len(s)):
    #to check one
    if(s[i]) == '1':
        count += 1
        #to update the length
        if(count > length):
            length = count
    else:
        count = 0

print(length)
