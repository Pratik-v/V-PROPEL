'''Increment mixed string is an operation which operates on two strings S1 and S2 of same length to generate a new string S3. The letters in odd position of S3 is one more 
than the corressponding letter in S1 and the letters in even position of S3 is one more than the corressponding letter in S2. For example, if S1 = ‘amey’ and S2 = ‘dhft’ 
then S3 = ‘bifu’. For letter ‘z’, letter ‘a’ is one more than it.

 

Fibanocci increment mixed string is operation which operates on the last two strings in the series. Given two strings, S1 and S2 write a code to generate the nth element 
using Fibanocci increment mixed string operation. The given strings S1 and S2 are the first two elements in the Fibanocci increment mixed string series. Third element in 
the series is found by applying increment mixed string operation for first two elements.

 

If S1 = ‘amey’ and S2 = ‘dhft’ then the first five elements in the series are as follows:

amey

dhft

bifu

ejgv

ckgw

 

Input Format

First line contains the string S1

Next line contains the string S2

Next line contains the value of n

Output Format

Print the nth element in the Fibanocci increment mixed string series'''

S1=input()
S2=input()
n=int(input())
l=[S1,S2]
c=0
while(c<n-2):
    S3=""
    for i in range(len(S1)):
        if(i%2==0):
            if(ord(S1[i])>=122):
                S3+=chr((ord(S1[i])%122)+97)
            else:
                S3+=chr(ord(S1[i])+1)
        else:
            if(ord(S2[i])>=122):
                S3+=chr((ord(S2[i])%122)+97)
            else:
                S3+=chr(ord(S2[i])+1)
    l.append(S3)
    S1,S2=S2,S3;
    c+=1;
print(l[n-1])
