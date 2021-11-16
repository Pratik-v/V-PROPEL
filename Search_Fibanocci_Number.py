'''Given an integer n, search for the set of all fibanocci numbers F = {f1∪f2∪f3∪...fn} where fi is the set of fibanocci numbers of length ‘i’ and present in the number ‘n’. 
A number in fi is formed by taking ‘i’ consecutive digits from ‘n’. For example, if the value of n is 121393 then f1 = {1, 2, 3}, f2 = {13, 21}, f3 = {}, f4 = {}, f5={} and 
f6={121393} hence F = {1, 2, 3, 13, 21, 121393}. If no fibanocci number is present then print None.

Input Format

First line contains a number, n

Output Format

Print all the fibanocci numbers present in n, in ascending order. Print one number in one line. If no fibanocci number is present then print None.'''

def fibonacci():
    l=[0,1]
    j=0
    while(j<n):
        j=l[-1]+l[-2]
        l.append(j)
    return l
n=int(input())
c=0
for i in fibonacci()[2:]:
    if(str(i) in str(n)):
        print(i)
        c+=1
if(c==0):
    print(None)
