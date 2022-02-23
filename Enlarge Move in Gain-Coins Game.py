'''Gain-Coins is a mxn board game, in which the number of coins in each square increases during enlarge move. The number of coins on each square ‘s’ which is row ‘r’ and 
column ‘c’ increases by the maximum number of coins in the row ‘r’ and also increases by the minimum number of coins in the column of ‘c’. Given the number of coins in the 
board write a C program to print the number of coins in the board after enlarge move. For example if the number of coins in a 3X3 board is:

2 3 4

5 7 3

3 8 1

Then after enlarge move the number of coins will be:

8 10 9

14 17 11

13 19 10

Input Format

First line contains the number of rows in the board, r

Next line contains the number of columns in the board, c

Next ‘r’ lines contain the number of coins on each row separated by a space

Output Format

Print the number of coins on the board after enlarge operation

Print the number of coins in one row on each line separated by a space

Note: A space is present at the end of each row'''

r,c=int(input()),int(input())
rw=[list(map(int,input().split())) for i in range(r)]
cw=[[i[j] for i in rw]for j in range(c)]
rr=[]
for i in range(r):
    temp=[]
    for j in range(c):
        temp.append(rw[i][j]+max(rw[i])+min(cw[j]))
    rr.append(temp)
for i in rr:
    print(*i,end=" \n")
