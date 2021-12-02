'''Kartik has been given many words to type. For each word he types he consumes some time depending on the character that is going to be pressed.
For simplicity, we are going to assume that all the words he has to type consist of only 4 letters 'd' , 'f', 'j' and 'k'.
He can type 'd' and 'f' with the left hand and the letters 'j' and 'k' using the right hand.
When typing a word he takes, he takes 2 seconds to type the first character, for each of the other character he types, he takes 2 seconds to type if the character uses other 
hand and 4 seconds if the character uses the same hand.
If he has typed a word already then he can type that word in half the time taken to type it for the first time.
Given some words, calculate the total time taken to type all the given words.

Input:
The first line of input contains 'N', the number of words to type.
Subsequence N lines each contain a string denoting the word that Kartik has to type.

Output:
Print one single line containing the time taken to type all the words.

Example:
Input:
4
dfjk
ddd
jkd
dfjk

Output:
36'''

N=int(input())
l=[input() for i in range(N)]
ss=[]
left,right='df','jk'
for i in range(len(l)):
    if(l[i] in l[:i]):
        ss.append(ss[l.index(l[i])]//2)
    else:
        s=0
        for j in range(len(l[i])):
            if(l[i][j] in left):
                if(j==0):
                    s+=2
                else:
                    if(l[i][j-1] in left):
                        s+=4
                    else:
                        s+=2
            if(l[i][j] in right):
                if(j==0):
                    s+=2
                else:
                    if(l[i][j-1] in right):
                        s+=4
                    else:
                        s+=2
        ss.append(s)
print(sum(ss))
