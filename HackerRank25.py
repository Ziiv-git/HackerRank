
'''
Task:- A prime is a natural number greater than 1 that has no positive divisors
other than 1 and itself. Given a number,n, determine and print whether it's Prime or Not Prime.

Note: If possible, try to come up with a 0(square root(n)) primality algorithm,
or see what sort of optimizations you come up with for an O(n) algorithm. Be sure
to check out the Editorial after submitting your code!

Input Format

The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines contains an integer,n, to be tested for primality.

Output Format

For each test case, print whether n is Prime or Not Prime on a new line.

Sample Input

3
12
5
7

Sample Output

Not prime
Prime
Prime
Explanation

Test Case 0: n = 12.

12 is divisible by numbers other than 1 and itself (i.e.: 2, 3, 6 ), so we print
Not Prime on a new line.

Test Case 1: n = 5.

5 is only divisible 1 and itself, so we print Prime on a new line.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
t=int(input())
def isPrime(data):
    data = int(data)
    if data < 2:
        return False
    v=int(math.sqrt(data))
    for i in range(2,v+1):
        if data%i==0:
            return False;
    return True;
for i in range(t):
    if isPrime(input()):
        print ("Prime")
    else:
        print ("Not prime")
