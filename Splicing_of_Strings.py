'''Let S1 and S2 be any two strings with few symbols in common. If there are duplicates in S1 or S2 then remove them. During the duplicate removal process retain the first 
occurence of the characters. For example, if element is the string then after duplicates removal it will be elmnt.

Crossover is the process of joining two strings S1 and S2 with pivot as one of the common characters of S1 and S2. If ‘α’ be a common character of S1 and S2 such that 
S1 = Prefix(S1)αSuffix(S1) and S2 = Prefix(S2)αSuffix(S2). Here Prefix(S1) is the sequence of characters that appear before α in S1 and Suffix(S1) is the sequence of 
characters that appear after α in S1. Then crossover(S1,S2, α) = Prefix(S1)+α+Suffix(S2) and Prefix(S2)+α+Suffix(S1). Splicing is the process of forming all posible new 
strings from S1 and S2 by performing crossover of S1 and S2 with all common characters.

For example, consider two strings abcdce and ecfgdc then after duplicate removal the strings are abcde and ecfgd. There are three common characters ‘c’ and ‘d’.

crossover(s1,s2,c) = abcfgd and ecde

crossover(s1,s2,d) = abcd and ecfgde

crossover(s1,s2,e) = abcdecfgd and e

and splicing (s1, s2) = abcfgd, ecde, abcd, ecfgde, abcdecfgd, e

Input Format

First line contains the first string, S1

Second line contains the second string, S1

Output Format

Print each newly formed string formed by splicing in sorted order. Print one new string in one line'''

def remdup(f1):
    f2=""
    for i in f1:
        if not i in f2:
            f2+=i
    return f2
    
def common(f1,f2):
    l=[]
    for i in f1:
        if(i in f2):
            l.append(i)
    return l
    
def crossover(f1,f2,f):
    return f1[:f1.index(f)]+f2[f2.index(f):]

s1,s2=remdup(input()),remdup(input())
l=[]
for i in common(s1,s2):
    l.append(crossover(s1,s2,i))
    l.append(crossover(s2,s1,i))
print(*sorted(l),sep="\n")
