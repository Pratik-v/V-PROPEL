'''In a game for kids under age seven, m*n kids are made to sit in a room where there are ‘n’ chairs arranged in ‘m’ rows. The game organizers has got ‘m*n’ chits in which 
either one of the two numbers ‘p’ or ‘q’ is written. Each kid is asked to pick a chit. A lot is taken by the coordinator which contains the lucky number ‘l’ (Value of 'l' will 
be either 'p' or 'q'). Then it is declared that “Chit Transition” takes place for few kids. If the lucky number ‘l’ is equal to ‘p’, during chit transition, a kid ‘k’, sitting 
in the row ‘r’ and column ‘c’ with number ‘p’ is given ‘q’ when one of the following criteria is satisfied:

(i) If atleast one of the kid sitting in the row ‘r’ has ‘q’

(ii) If atleast one of the kid sitting in the column ‘c’ has ‘q’

After this Chit transition phase, the kids with number ‘p’ are declared as winners. For example, if there are 3*3 kids, chit numbers as 3 and 5 seated with original chit 
number as follows:

3 5 3

3 3 3

3 5 5

If the lucky number taken by coordinator is 3 then the chit number of the kids after “Chit Transition” phase will be:

5 5 5

3 5 5

5 5 5

Now the kid sitting in the second row and first column is the winner. Sometimes there can be more than one winner in this game and sometimes there may not be any winner in 
this game also. Print the row and column position of all the winning kids and when there are no winners print ‘No winner’.

Input Format

First line contains the number, m

Next line contains the number, n

Next line contain the number, p

Next line contain the number, q

Next ‘m’ lines contain the chit number of ‘n’ kids seated on each row separated by a space

Next line contains the lucky number, l

Output Format

Print the row and column position of winning kids in order. Print the position sorted row wise, when row of more than one position is same print them sorted column wise and 
Print ‘No winner’ when no one has won the game'''

m,n,p,q=int(input()),int(input()),int(input()),int(input())
mn=[list(map(int,input().split())) for i in range(m)]
mnr=mn.copy()
mnc=[[mnr[i][j] for i in range(m)] for j in range(n)]
l=int(input())
mn1=[x[:] for x in mn]
for i in range(m):
    for j in range(n):
        if(mn[i][j]==p and p==l):
            if(q in mnr[i]) or (q in mnc[j]):
                mn1[i][j]=q
        if(mn[i][j]==q and q==l):
            if(p in mnr[i]) or (p in mnc[j]):
                mn1[i][j]=p
flag=0
#print(mn,mnr,mnc,mn1)
f=[]
for i in range(m):
    for j in range(n):
        if(mn1[i][j]==l):
            f.append([i+1,j+1])
            flag=1
if(flag==0):
    exit(print("No winner"))
f.sort(key = lambda x: x[1])
f.sort()
for i in f:
    print(*i)
