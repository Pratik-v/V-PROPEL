'''After solving yesterday's problem, Adarsh is now enjoying and decides to go on a picnic.
All of his classmates are divided into 'N' groups. Cabs are going to be ordered depending on the number of students.
The classmates which belong to the same group have to travel together. Each cab can carry at most 4 students. What is the minimum 
the number of cabs needed if all classmates of each group should travel in the same car and one car can take more than one group.

Input Format:
The first line of the input contains N, the number of groups
The second line contains N space-separated integers, ith of them denoting the size of the ith group

Output Format:
Print one line containing a single integer denoting the minimum number of cabs required.

Constraints:
1 <= N <= 50
1 <= size of each group <= 4

Examples:
Input:
5
1 2 4 3 3
Output:
4

one cab will be required by the group having 4 people
one cab will be required by a group of people having 3 and 1 person(s).
Now we are left with two groups of size 2 and 3.
Both of them cannot travel in the same cab because the size will become 3 + 2 = 5, and since each cab can carry only 4 people at max
we will be requiring a new cab for both these groups. Hence the minimum number is 4.'''

N=int(input())
l=list(map(int,input().split()))
c=0
while(c<N):
    for i in l:
        k=[]
        k1=[]
        flag=0
        for j in l[:l.index(i)]+l[l.index(i)+1:]:
            if(i+j<=4):
                k.append(i)
                k1.append(j)
                flag=1
        if(flag==1):
            l.remove(max(k))
            l.remove(max(k1))
            l.append(max(k)+max(k1))
    c+=1
print(len(l))
