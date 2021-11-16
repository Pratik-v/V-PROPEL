'''A sequence of numbers is called cute if all the numbers in the sequence are made of only two digits, 8 and 9.
Example of a cute sequence is: 8, 9, 88, 89, 98, 99…. and so on.
A number is called beautiful if it is divisible by any number which is part of the cute sequence.
For example: 8 (divisible by 8), 9(divisible by 9), 889 (divisible by 889),  10668 (divisible by 889) are beautiful numbers. Given a number, n, 
write a code to print “beautiful” (without quotes) if it is divisible by any number that contains only 8 or 9 or both and print -1 otherwise.

Input Format:

Input contains one single line denoting the number, n


Output Format:
Print "beautiful" if the number is a beautiful number and -1 otherwise

Constraints:
1 <= N <= 999999999999999999'''

import itertools as Z
def check(l):
    for i in l:
        if(n%int(i)==0):
            exit(print("beautiful"))
# def check2(c):
#     if(c==1000):
#         exit(print(-1))
n=int(input())
l1=['8'*i for i in range(1,19)]
l2=['9'*i for i in range(1,19)]
l3=[]
for i in l1:
    for j in l2:
        l3.append(i+j)
check(l1+l2+l3)
c=0
# for j in l3:
#     for i in Z.permutations(j):
#         c+=1
#         check2(c)
#         if(n%int(''.join(i))==0):
#             exit(print("beautiful"))
print(-1)
