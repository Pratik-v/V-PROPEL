#QUESTION:
'''A proper factor of a number is a factor of the number other than itself. Given a collection of numbers, a number n1 in position ‘i’ is said to be principal number if 
the largest proper factor of all numbers in position > i is lesser than or equal to the largest proper factor of n1. The last number in the collection is a principal number. 
For example, given five numbers 29, 15, 5, 9 and 11, the output should be 15, 9 and 11.

Input Format

First line contains the number of elements, n

Next ‘n’ lines contain the elements in the collection

Output Format

Print the principal numbers one on each line'''

#CODE:
def proper(n):
    for i in range(1,n):
        if(n%i==0):
            factor=i
    return factor
n=int(input())
l=[int(input()) for i in range(n)]
pf=[proper(i) for i in l]
for i in range(n):
    flag=0
    for j in range(i+1,n):
        if(pf[i]<pf[j]):
            flag=1
    if(flag!=1):
        print(l[i])
