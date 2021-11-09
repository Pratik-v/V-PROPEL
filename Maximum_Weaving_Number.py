'''Given two numbers A=a1a2...an and B= b1b2...Bm, we can weave these two numbers to produce the following numbers.

a1b1a2b2...anbnb(n+1)...bm,, if m>n

a1b1a2b2...ambma(m+1)...an if m<n

a1b1a2b2...anbn if m=n.

Similarly, we can also get b1a1b2a2.... as above.

We can also start weaving from the end. By weaving from the end, we can form the words: anbnb(n-1)a(n-1)... , bnanb(n-1)a(n-1)...

Thus, by weaving A and B, four new numbers are formed: weaving from the beginning, starting with A, weaving from the beginning, starting with B, weaving from the end, 
starting with A, weaving from the end, starting with B. While weaving two numbers A and B, if all the digits of A are weaved and some more digits are there in B, 
the remaining digits of B are just appended at the end. For example, if A = 27 and B = 54 then there are four numbers that can be woven

2574

5247

7425

4752

and maximum out of these is 7425

Given two numbers A and B, write a code to compute the numbers woven by A &B and find the maximum woven number.

Input Format:

First line contains the number A

Next line contains the number B

Output Format:

Print the maximum woven number

 

Note: Input and Output may be as large as 10^10 choose appropriate data type'''

def woven(a,b):
    s=""
    for i in range(min(len(a),len(b))):
        s+=a[i]
        s+=b[i]
    for i in a+b:
        if not i in s:
            s+=i
    return s
def call(A,B):
    l=[woven(A,B),woven(A[::-1],B[::-1]),woven(B,A),woven(B[::-1],A[::-1])]
    return max(l)
A,B=input(),input()
print(call(A,B))
