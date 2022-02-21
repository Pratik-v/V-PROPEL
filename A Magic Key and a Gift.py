'''An angel gave box with ‘N’ pearls in it and a magic key ‘K’ to a peasant. The angel asked the peasant to apply the key repeatedly till the box gets opened.

The box will get opened only when it becomes empty and the key performs a magic for each time the peasant applies it to the box. Each time when the key is used on the magic box, 
the following things happen:

(i) Pearls in the box will be grouped into ‘G’ groups such that each group contains exactly ‘K’ pearls.

(ii) The magic box piles up the pearls left ungrouped into a safety locker inside it

(iii) After piling up, the box will contain lesser pearls equal to the number of groups ‘G’ formed in the current step

When the box becomes empty the box opens with the pearls in the safety locker and given as gift to the peasant.

Given the number of pearls, ‘N’ and the key ‘K’, write a C program to display the number pearls that got saved in the locker from the recent time to the initial time and the 
total number of pearls that is given as gift for the peasant.

For example, if ‘N’ is 200 and ‘K’ is 7, then the locker displays the number of pearls saved from recent time to the initial time as 404 and the peasant gets 8 pearls as his 
gift.

Input format:

First line contains the number of pearls ‘N’ in the magic box

Next line contains the key value ‘K’

Output format:

In the frist line, print the number of pearls saved from recent time to the initial time in the same line continuously

In the next line print the number of pearls given as gift for the peasant'''

n,k,s,ss=int(input()),int(input()),"",0
while(n>0):
    s+=str(n%k)
    ss+=n%k;
    n//=k
print(s[-1::-1],ss,sep="\n")
