'''Consider n numbers. Average of the given n numbers is the sum of all the numbers divided by n. Moving average of size k, k<=n, written as Mvk , is the average of the first 
k numbers among the n numbers. For a number with n digits, there will be n moving averages. Grand Moving average is the average of all the possible moving averages. 
If we have the numbers 1,7,8,9; moving average of size 1 is 1. Moving average of size 2 is (1+7)/2= 4. Moving average of size 3 is (1+7+8)/3=5.33; 
Moving average of size 4 is (1+7+8+9)/4 = 6.25. Grand moving average is (1+4+5.33+6.25)/4= 16.58/4=4.14

Given n numbers, Write the pseudocode and the code to compute the Grand Moving Average of the given numbers. The grand moving average should be printed in two decimal format.

Input format

First line contains the number of numbers, n

Next ‘n’ lines contain the numbers in the collection

Output format:

Print grand Moving Averages in two decimal format

Illustration :

Input

4

1

7

8

9

Output

4.14'''

n=int(input())
l=[int(input()) for i in range(n)]
k=[sum(l[:i+1])/(i+1) for i in range(len(l))]
print("{:.2f}".format(sum(k)/n))
