#QUESTION:
'''Rahul is playing a game known as skipping stones. In this game, in order to reach the end he can either jump past 1 stone or 2 stones at a time. He enjoyed playing the game 
but wonders in how many ways can he reach to the Nth step. Please help Rahul in finding the answer to this problem.

Input Format:
The first line containing Q, denoting the number of queries to answered.
Each of the next Qi, lines denote the value of Nth stone.

Output:
Print Q lines, each containing the value of ith query on a single line. If the answer is greater than 32 bit integer output it modulo 10^9+7.

Constraints:
1 <= Q <= 1000
The value of N in each query can go upto 1000.


Example:
Input:
2
1
4
Output:
1
5

Explanation:
There are 5 ways in which Rahul can reach to the 4th stone, these are:
1. Going 1 by one to each stone: (1,1,1,1)
2. (2,2)
3. (1,2,1)
4. (2,1,1)
5. (1,1,2)'''

#CODE:
