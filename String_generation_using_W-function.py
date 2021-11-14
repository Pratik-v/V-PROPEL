'''Using an N-function, every letter of English alphabet (either upper case or lower case) can be represented as a number that corresponds to its position in the 
English alphabet. For example, ‘A’ is represented by 1, ‘z’ by 26. This is written as N(A)=1, N(a)=1. In the same way, using a W-function, a number k in the range, 
from 1 to 26 (both included) , is represented by the symbol whose positional index in the English alphabet, is k. This is written as W(25)=y.

From an integer n, two strings W1 and W2 may be generated in such a way that every character ‘c’ in W1 or W2, taken in order, is equal to W(k)=c where k is a single digit for 
generating W1 and it is a two digit number for generating W2, that occurs in order in the given integer ‘n’. When the two digit number, k is greater than 26 take the letter 
corresponding to modulus 26 of k.

Given an integer ‘n’ which does not have any zero as its digits, write an algorithm and the pseudocode to generate the two strings that can be formed from the number n using 
W-function.

Print both the words in lower case letters

For example, if n = 1234 then words are generated from n as follows.

1-2-3- 4 generates abcd

12-23-34 generates lwh

When n= 491

4-9-1 generates dia

49-91 – generates wm

Input format :

First line contains a number, n

Output format

Print W1 in first line

Print W2 in second line'''

#code
n=input()
for i in n:
    print(chr(int(i)+96),end='')
print()
for i in range(len(n)-1):
    if(int(n[i:i+2])<=26):
        print(chr(int(n[i:i+2])+96),end='')
    else:
        print(chr(int(n[i:i+2])%26+96),end='')
