#QUESTION:

'''Given an integer ‘n’ where n>=1, write a C code to check whether there exist a smallest number ‘S’, where S<=107 and S is divisible by all even numbers ‘m’ where 1<=m<=n.

For example, when n = 10, the smallest number divisible by all even numbers 2, 4, 6, 8 and 10 is 120. If no such number exist then print ‘No such number in range’.

Input Format

First line contains the number, n

Output Format

Print either the number that is divisible by all even numbers less than ‘n’ or print No such number in range

'''

#CODE:

n=int(input())
e=[i for i in range(2,n+1,2)]
l,i=1,2
while(i!=n):
    c=0
    for j in range(len(e)):
        if(e[j]%i==0):
            e[j]//=i
            c=1
    if(c==1): l*=i
    else: i+=1
if(l>10**7):
    print("No such number in range")
else:
    print(l)
