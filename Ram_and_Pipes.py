'''Ram is a plumber who is working at a construction site where he has to build the entire piping system of the site. He has small pipes of various lengths which he can use 
to build a long pipe. However, whenever he wants to join two pipes there is an associated cost due to welding, raw material etc. The cost of joining two pipes is equal to 
the lengths of the two pipes being joined.

Ram really has a tight budget and wants your help in minimizing the overall cost of combining all the pipes.

Input format:

The first line contains a single integer ‘N’ denoting the number of pipes available.

Next N lines each contain a single integer denoting the length (L) , of the ith pipe

Output format:

Print a single line containing 1 integer, the minimum cost to join all pipes

Constrains:

1 <= N <= 500000

1 <= L <= 500

Examples:

Sample input 1:

2

1

2

Sample output 1:

3

Explanation

The minimum cost to join these pipes will be 1 + 2 = 3

Sample Input 2:

3

1

2

3

Sample Output 2:

9

Explanation:

We combine 1 and 2, and get a pipe of length 3 with a cost of 3

Now, we have two pipes of length 3 each, so the cost of joining these two

Pipes will be 3 + 3 = 6

So total cost = 6 + 3 = 9.

Hint: If you think that your logic is correct and you’re still getting TLE, then you should consider searching online for some data structure implemented by a python 
module (heapq or PriorityQueue) and understand how they can help you in solving this problem efficiently with the given constraints. You will get to know more in your 
Data Structures & Algorithms course, but if you are able solve this question now, excellent!'''

N=int(input())
L=[int(input()) for i in range(N)]
k=0
if(len(L)==1):
    exit(print(L.pop()))
while(L!=[]):
    L.sort()
    s=L.pop(0)
    if(L!=[]):
        p2=L.pop(0)
        s+=p2
        k+=s
        L.append(s)
    else:
        break
print(k)
