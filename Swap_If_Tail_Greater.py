#QUESTION:
'''To check if a number n1 is tail greater than another number n2, one has to compare the digits from the end of the numbers. When the digits in position ‘i’ are same for 
the numbers then the previous digits has to be compared till a conclusion can be made. If the elements in position ‘i’ and ‘i+1’ are same then do not swap.

Input Format

First line contains the number of elements in the collection, n

Next ‘n’ lines contain the numbers in the collection

Output Format

Print the elements after swapping if not in tail greater order mentioned. Print one number in one line

For example, 13 is greater than 41 since 3 the last digit of 13 is greater than 1 which is last digit of 41. 253 is greater than 153 but lesser than 18.

Given a collection of n integers with same number of digits, write a C code to swap adjacent elements if element in position ‘i+1’ is not tail greater than the element 
in position ‘i’. For example, given five integers 223, 131, 145, 144 and 315 after swap is done elements will be 131, 223, 144, 315, 145.'''

#CODE:
n=int(input())
l=[input() for i in range(n)]
for i in range(n-1):
    if(l[i]==l[i+1]):
        continue
    k=-1
    while(abs(k)!=len(l[i])):
        if(l[i][k]<l[i+1][k]):
            break
        if(l[i][k]>l[i+1][k]):
            l[i],l[i+1]=l[i+1],l[i]
            break
        if(l[i][k]==l[i+1][k]):
            k-=1
print(*l,sep="\n")
