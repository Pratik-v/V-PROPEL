'''Matrix Difference is a binary operation which operates on two matrices of any dimensions and represented by the symbol ‘~’. It is defined as follows:

If M3 = M1~M2 then M3[i,j] = M1[i,j] if M1[i,j] ∉ M2 and M3[i,j] = 0 otherwise where M1[i,j] ∉ M2 indicates that M1[i,j] is not an element of matrix M2. 
Given two matrices M1 and M2 write a code to find M1~M2.

For example, if M1 is a 3X3 matrix as shown below:

4 5 7

1 9 11

12 3 2

and M2 is a 2X2 matrix as shown below:

15 5

11 2

then M3 should be

4 0 7

1 9 0

12 3 0

This operation is not commutative. M2~M1 will have the following elements:

15 0

0 0

Note:

1. Only valid input is given for the problem

2. In the output, last element of each row is followed by a space

Input Format

First line contains the number of rows in M1, r1

Second line contains the number of columns in M1, c1

Next r1 lines contain the elements in one row of M1 separated by a space

Next line contains the number of rows in M2, r2

Next line contains the number of columns in M2, c2

Next r2 lines contain the elements in one row of M2 separated by a space

Note that only valid input is given for the problem

Output Format

Print each row of Matrix M3 in one line and elements in a row should be separated by a space'''

r1=int(input())
c1=int(input())
M1=[input().split() for i in range(r1)]
r2=int(input())
c2=int(input())
M2=[input().split() for i in range(r2)]
M22=[]
for i in M2:
    for j in i:
        M22.append(j)
for i in M1:
    for j in i:
        if(j in M22):
            print(0,end=" ")
        else:
            print(j,end=" ")
    print()
