#QUESTION
'''You are given a sequence of integers. You want to find out if all the numbers have a common divisor. Common divisor should be greater than 1.
If there exists such a number, print "YES", otherwise print "NO".

Input Format:
The first line of the input contains an integer N, denoting the number of elements in the array.
The second line contains N space-separated integers.

Output Format:
Print "YES" or "NO" on a single line(without quotes) according to the above condition.


Example:
Input:
3
2 3 4
Output:
NO

Input:
5
5 10 15 20 25
Output:
YES'''

#CODE
def f(f1):
    l=[]
    for i in range(2,f1+1):
        if(f1%i==0):
            l.append(i)
    return l
n=int(input())
m=list(map(int,input().split()))
k=[]
for i in m:
    for j in f(i):
        k.append(j)
for i in k:
    if(k.count(i)==n):
        exit(print("YES"))
print("NO")
