'''A farmers takes chicken and duck eggs in ‘n’ baskets. In two baskets he has got duck eggs and rest of the bags he has chicken eggs. Number of eggs in each basket 
is distinct. He tells that number of chicken eggs is twice as that of number of duck eggs. Given the name of the ‘n’ baskets and number of eggs in them, write a code to 
print the name of baskets with duck eggs and name of basket with chicken eggs. If there can be more than one combination in which duck eggs can be there, consider the 
first basket name which comes first in the input order

Input Format

First line contains the number of baskets, n

Next ‘n’ lines contain the name of the baskets and the number of eggs in them

Output Format

Print name of baskets with duck eggs separated by a space in the first line

Print name of baskets with chicken eggs separated by a space in the next line

Print the name of the baskets in the order of their input and there is no space at the end of the lines

Example1

Input

5

B1 5

B2 12

B3 14

B4 23

B5 6

Output

B3 B5

B1 B2 B4'''
#We Can Do This With Combination as well as by permutation ...
from itertools import permutations as p
n=int(input())
l=[input().split() for i in range(n)]
name=[i[0] for i in l]
count=[int(i[1]) for i in l]
flag=0
duck=0
f1=[]
for i in range(n):
    for j in p(count,i):
        if(sum(j)==sum(count)//3):
            duck=j
            flag=1
            break
    if(flag==1):
        break
for i in duck:
    f1.append(name[count.index(i)])
print(*f1)
for i in name:
    if i not in f1:
        print(i,end=' ')
