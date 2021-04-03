'''
Objective

Today’s challenge puts your understanding of nested conditional statements to the
test. You already have the knowledge to complete this challenge, but check out the
Tutorial tab for a video on testing!


Task

Your local library needs your help! Given the expected and actual return dates
for a library book, create a program that calculates the fine (if any).
The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be
charged (i.e.: fine = 0).
If the book is returned after the expected return day but still within the same
calendar month and year as the expected return date, fine = 15 Hackos x (the number of days late).
If the book is returned after the expected return month but still within the
same calendar year as the expected return date, the fine = 500 Hackos x (the number of months late).
If the book is returned after the calendar year in which it was expected,
there is a fixed fine of 10000 Hackos.

Input Format

The first line contains 3 space-separated integers denoting the respective day,
month, and year on which the book was actually returned.
The second line contains 3 space-separated integers denoting the respective day,
month, and year on which the book was expected to be returned (due date).


Constraints

1 <= D <= 31
1 <= M <= 12
1 <= Y <= 3000
It is guanranteed that the dates will be valid Gregorian calendar dates.

Output Format

Print a single integer denoting the library fine for the book received as input.


Sample Input

1
2
9 6 2015
6 6 2015

Sample Output

1
45

'''


actually = str(input()).split(" ")
da = int(actually[0])
ma = int(actually[1])
ya = int(actually[2])

expected = str(input()).split(" ")
de = int(expected[0])
me = int(expected[1])
ye = int(expected[2])

fine = 0

if ya > ye:
    fine = 10000
elif ya == ye:
    if ma > me:
        fine = (ma - me) * 500
    elif ma == me and da > de:
        fine = (da - de) * 15

print(fine)
