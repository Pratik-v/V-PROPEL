'''Ramu makes a travel to one his office in a hilly region by his car. Given the height of his current location above sea level every few minutes after he starts the travel, 
write a code to check the number of up moves and down moves. First move is always up move.

For example, if 12 points are given as follows 45, 60, 82, 72, 65, 32, 53, 84, 103, 110, 89, 95 then there are 3 up moves and 2 down moves.

Input Format

First line contains the number of current locations of Ramu, n

Next line contains ‘n’ height of locations separated by a space

Output Format

Print the number of Up moves and number of Down moves separated by a space'''

n=int(input())
l=list(map(int,input().split()))
ui,li=0,0
uu,ll=[],[]
for i in range(1,n):
    if(l[i]-l[i-1]>0):
        li+=1
        uu.append(ui)
    else:
        ll.append(li)
        ui+=1
print(len(set(uu)),len(set(ll)))
