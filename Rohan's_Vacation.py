'''Rohan was going on a long vacation across various cities in the world. He had made an itinerary containing all the information about his journey. He had flight tickets 
booked as well.

Unfortunately, at the last minute, someone just ran into him and all his tickets fell on the floor.

Help him to find the correct order of all the tickets by finding the correct path from source to destination.

Input Format:

First line of the input contains a number N, indicating the number of tickets he has.

Next lines each contain two strings made of alphabets, each separated by a space, the src(source) and the dest (destination).

Output format:

Print a single line containing the entire journey plan (itinery) of Rahul.

Constraints:

1 <= N <= 500

1 <= len(src), len(dest) <= 50

Source and destination strings are made up of alphabets(uppercase/lowercase).

Example Input:

3

DEL KOL

MAA DEL

KOL GOA

Example Output:

MAA DEL KOL GOA

Explanation:

Given the tickets from DEL to KOL, MAA to DEL, KOL to GOA,

If we arrange the properly, we can see that Rohan starts from MAA then goes to DEL,

And then from DEL he has ticket to KOL and from KOL he has ticket to GOA, so we print his entire itinerary.'''

def path(a,b):
    for i in l:
        if(i[0]==a):
            print(i[1],end=" ")
            if(i[1]==b):
                exit(0)
            else:
                path(i[1],b)
n=int(input())
l=[input().split() for i in range(n)]
src=[i[0] for i in l]
dec=[i[1] for i in l]
for i in src:
    if not i in dec:
        s=i
for j in dec:
    if not j in src:
        d=j
print(s,end=" ")
path(s,d)
