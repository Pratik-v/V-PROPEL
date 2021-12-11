#QUESTION:
'''You are given the top view of a ground, where there are two values: '0' and '1'. Each '1' denotes that there is a person standing at that 
position in the ground. Recently Raman was asked to find the number of distinct pairs of people who have given manhattan distances between them.
Raman doesn't like to disappoint and hence he has come to you for help.

For more information on Manhattan distance, see here.


Input Format:
The first line of the input contains two space-separated integers 'n' and 'm' denoting the number of rows and number of columns in the ground.
Then 'n' lines follow, each of which contains a string containing '0's and '1's.
The next line contains the value of 'q' denoting the number of queries.
Each of the following lines contain one integer denoting the distance

Output Format:
Print q lines, each containing the number of distinct pairs of people who have manhattan distance equal to the given manhattan distance.

It is guaranteed that the distance given in query will be between 1 and n+m-2 (both inclusive).

Example:
Input:
3 4
0001
0100
0010
5
1
2
3
4
5

Output:
0
1
2
0
0'''

#CODE:
r,m=map(int,input().split())
l=[input() for i in range(r)]
a=int(input())
l1=[int(input()) for i in range(a)]
l2,l3=[],[]
for x in range (r):
    for y in range (m):
        if(l[x][y]=='1'):
            l2.append([x,y])
for i in range (len(l2)):
    for j in range (i+1,len(l2)):
        l3.append(abs(l2[i][0]-l2[j][0])+abs(l2[i][1]-l2[j][1]))
for i in l1:
    if (i in l3) : print(l3.count(i))
    else : print(0)
