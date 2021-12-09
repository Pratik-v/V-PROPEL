'''In an industry, robots are employed to bring specified number of nuts, ‘n’ to its current location. Different numbers of nuts are packed in ‘m’ packages and kept in a rack 
at a location inside the industry.

Robot can make only one fetch operation. In a single fetch operation, they can fetch packages from one rack or more than one adjacent racks only. Size of the fetch operation 
is the number of packages taken by the robot. Power consumed by the robot increases with the size of the fetch operation. When fetch size is same, fetching from rack(s) with 
lesser rack numbers consume less power than fetching from higher rack numbers.

Given the number of nuts required, ‘n’ and the number of nuts in each of ‘m’ packages, write a code to print the number of nuts in the packages that are to be taken by the 
robot so that it consumes least possible power. If the number of nuts cannot be fetched by the robot print ‘Not possible’.

For example, if the number of nuts required is 10 and the nuts are packed in five pacakages as follows:

2 3 6 4 10

Then 10 is the best possible package of nut(s) that shall be taken. If 18 nuts are required and the nuts are packed in five pacakages as follows:

2 3 6 4 10

then print ‘Not possible’.

Input Format

First line contains the number of nuts required, n

Next line contains the number of packages, m

Next line contain the number of nuts in m packages separated by a space

Output Format

Print the nuts in the packages that has to fetched and print Not possible if the robot cannot fetch'''

n,m=int(input()),int(input())
l=list(map(int,input().split()))
ll=[]
for i in range(m):
    for j in range(m,i,-1):
        if(sum(l[i:j])==n):
            ll=l[i:j]
if(ll!=[]): print(*ll)
else: print("Not possible")
