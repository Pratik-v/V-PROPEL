#QUESTION:
'''Note: Students using C, C++ or Java to solve the problem have to use long int for the variables instead of int. The results are different and using long int gives the correct 
answer. The problem description is also modifed to add more clarity of what has to be done to handle overflow. Please try again with these suggestions so that your code may pass 
now

In the stock market of the city Knowhere, the stock prices of a given day is calculated as 3 times the price of previous day plus 4 times the price of the day before yesterday.
Given the prices on day 1 and day 2, answer Q queries asking you about the price of the stock on the Nth day.

Input Format:
The first line of the input contains two space-separated integers A and B, denoting the initial price of stock on day 1 and day 2
The next line of the input contains an integer Q denoting the number of queries.
The next line contains Q space-separated integers each denoting the number of the day for which the stock price is asked.

Output Format:
Print one line containing Q space-separated integer, ith of them denoting the value of the stock price on ith day. Since there is a possibility of overflow of values while 
calculating price on ith day (i.e.) values may become larger than the value contained in 32 bit integer, so take modulo (10^9+7) wherever required.

Constraints:
1 <= A,B <= 10^5
1 <= Qi <= 10^3

Example:
Input:
1 2
3
1 2 3

Output:
1 2 10'''

#CODE:
A,B=map(int,input().split())
Q=int(input())
l=list(map(int,input().split()))
s=[A,B]
while(len(s)!=max(l)): s.append(3*s[-1]+4*s[-2])
for i in l:
    if(s[i-1]>2**32): print(s[i-1]%(10**9+7),end=" ")
    else: print(s[i-1],end=" ")
