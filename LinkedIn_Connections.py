'''LinkedIn Connections
Whenever two people are connected to each other on linkedin, they are considered as connections of each other. A term degree of connection is defined by the distance between 
a person and the connection. For example, if Rahul is connected to Neha and Neha is connected to Raj, in this case:

Connection: Degree

Neha-Raj: 1

Rahul-Neha: 1

Rahul-Raj: 2

Raj-Neha: 1

It is very important to grow your network on LinkedIn, and so in order to do this, one needs to send connection requests to different people. However, LinkedIn has a 
restriction in terms of a person to whom you can send a connection request. You can only send connection requests to people who are your 3rd degree connections, meaning 
that the distance between you and that person should be at most 3. Given the number of people on the linkedin platform and all the connections, answer n queries in which 
ith (1<= i <= n) query asks you if a connection request can be sent to the person or not.

Input Format:

First line of the input contains a single integer, the number of people: N

Second line of the input contains a single integer the number of connections: M

Next M lines contain two integers each, separated by space: (Xi Yi) ; 1 <= i <= M

Next line contains an integer, person who wants to send connection requests: K (1 <= K <= N)

Next line contains, one single integer, the number of queries, Q

Next Q lines, each containing an integer, jth (1 <= j <= Q) containing an integer L (1 <= L <= N)

Output Format:

Output Q lines each containing a string as follows:

“Yes” (without quotes), if the connection request can be sent.

“No” (without quotes), if the connection request cannot be sent.

 

Constraints:

1 <= 50 <= N

1 <= 50 <= M

1 <= 50 <= Q

Example:

Input:

12

13

1 2

1 5

2 4

5 3

5 6

1 7

7 8

1 9

9 10

7 10

10 11

11 12

4 6

1

3

2

12

11

Output:

yes

no

yes'''

def f1(x):
    for i in XY:
        if(i[0]==x):
            X.append(i)
            f1(i[1])
N,M=int(input()),int(input()) #number of people,number of connections
XY=[list(map(int,input().split())) for i in range(M)] #connections
K,Q=int(input()),int(input()) #person who wants to send connection requests,number of queries
L=[int(input()) for i in range(Q)] #queries
X=[]
f1(K)
for y in range(len(L)):
    for i in range(len(X)):
        if(X[i][0]==K):
            c=i
        if(X[i][1]==L[y]):
            if(i-c<4):
                L[y]='yes'
            else:
                L[y]='no'
for i in L:
    if(i=='yes'):
        print(i)
    else:
        print('no')
        
'''n = int(input())
m = int(input())


l1 = []
for i in range(m):
    l2 = list(map(int,input().split(" ")))
    l1.append(l2)

k = int(input())
q = int(input())

l2 = []

for i in range(q):
    l2.append(int(input()))

l1.sort()

l4 = []

for i in range(1,n):
    l3 = []
    for j in range(m):
       if(l1[j][0]==i):
           l3.append(l1[j][1])
    l4.append(l3)
# print(l1)
# print(l4)
l5 = []
l5.append(k)
for i in range(len(l4[k-1])):
    l5.append(l4[k-1][i])

count_list = len(l5)
count = 0

for j in range(count_list):
    for i in range(m):
        if(l1[i][0]==l5[count]):
            l5.append(l1[i][1])
        if(l1[i][1]==l5[count]):
            l5.append(l1[i][0])
    count+=1
#print(l5)

r1 = set(l5)
last_count = len(r1)
count=0
l6 = list(r1)
#print(l6)
for j in range(last_count):
    for i in range(m):
        if(l1[i][0]==l6[count]):
            l5.append(l1[i][1])
        if(l1[i][1]==l6[count]):
            l5.append(l1[i][0])
    count+=1


s1 = set(l5)

#print(s1)

for i in range(q):
    if l2[i] in s1:
        print("yes")
    else:
        print("no")'''
