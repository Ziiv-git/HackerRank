'''Recursion'''
# Objective
# Today, we are learning about an algorithmic concept called recursion. Check out the Tutorial tab for learning materials and an instructional video.
# Recursive Method for Calculating Factorial
#
# Function Description
# Complete the factorial function in the editor below. Be sure to use recursion.
# factorial has the following paramter:
# int n: an integer
# Returns
# int: the factorial of
# Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .

factorial = 1
# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


   or



import math
import os
import random
import re
import sys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = math.factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
