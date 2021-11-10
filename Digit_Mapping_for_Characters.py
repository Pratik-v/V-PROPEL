'''Given a string S with distinct letter find a mapping for each letter in it such that the number formed by replacing the letter with the numbers is a largest possible 
perfect square with different digits.

A number is said to be perfect square if the number is square of an integer. For example, if the word given is ‘care’ then the following map shall be done for the characters:

c – 9

a – 8

r – 0

e – 1

The number 9801 is a perfect square since 992 is 9801.

Input Format

First line contains the string for which numbers are to be assigned for characters

Output Format

Print character of the string and the number mapped for it separated by a space'''

import math
s=input()
for i in range(10**len(s),-1,-1):
    if(int(math.sqrt(i))==math.sqrt(i) and len(set(str(i)))==len(str(i))):
        k=str(i)
        break
for i in range(len(s)):
    print(s[i],k[i])
