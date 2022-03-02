'''Given the value of ‘n’ write a C program to print a special rectangular pattern with dots and starts. When the value of n is 5 the rectangle looks as below:

. . . . * . . . .

. . . * . * . . .

. . * . . . * . .

. * . . . . . * .

* . . . . . . . *

Input Format

First line contains the value of ‘n’

Output Format

Print the pattern appropriate to the value of ‘n’

Dots and stars are separated by one space and each row in the pattern is separated only by a new line character.'''

n=int(input())
l=[]
z=n-1
for i in range(n):
    k=""
    for j in range(n):
        if(j==z):
            k+='*'
        else:
            k+='.'
    k+=k[-2::-1]
    l.append(k)
    z-=1
for i in l:
    print(*i,sep=" ")
