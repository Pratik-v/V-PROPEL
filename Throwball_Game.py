#QUESTION:
'''A company is organizing a game for its employees on the occassion of new year celebrations. The game is conducted by a coordinator and has a group of ‘n’ players. 
In this game, all the players of the game are assured a prize money. The players are made to stand together one side of the net and as a first step the coordinator 
throws a ball towards them from the other side. The player ‘p’ who catches the ball first gets a prize money of ‘m’. Then the player ‘p’ is asked to go to the other 
side and throw the ball towards the rest of the players. This chain of throwing the ball continues such that the person who caught the ball in ith throw, throws the 
ball towards rest of the players in the i+1th throw. The chain continues till there is only one player left out in the group. The prize money for the players gets 
reduced by 2% for each catch. Given the maximum prize money ‘m’, name of the players in ascending order and the index of the name of the player who caught the ball 
when it was thrown by that particular player, name of the player who caught the ball in the frist throw, write a code to find out the prize money won by a player ‘x’.

 

For example, when there are seven players, maximum prize money is 5000, ball was caught by player at index 6 in the first thrown, and details of the players as follows, 
the prize money won by player A is 94% of 5000 and it is 4700.00

 

Index

Name of the Player 

Index of player who caught the ball 

1 A 3
2 B 5
3 C 2
4 D 7
5 E 0
6 F 4
7 G 1

The above table indicates that when the ball was thrown by the player ‘A’ it was caught by the player whose name is at index 3, when the ball was thrown by the player ‘B’ it was caught by the player whose name is at index 5 and so on. The player who caught the ball last has a 0 as the index of the player who caught the ball when it was thrown by that player.

 

Input Format

First line contains the maximum prize amount, m

Next line contains the number of players, n

Next ‘n’ lines contain the name of th players in ascending order and the index of name of the player to whom each player threw the ball, separated by a space

Next line contains the index of the name of the player who caught the ball first, 

Next line contains the name of the player whose prize money has to be found, x

 

Output Format

Print the prize money won by the player, x. Print only two decimal places

Example:

Input:

5000

7

A 3

B 5

C 2

D 7

E 0

F 4

G 1

6

A

Output:

6500.00'''

#CODE

def f(w,x,c):
    if l[w-1][0]==x:
        exit(print(format(((m*(100-(c*2)))/100),".2f")))
    else:
        f(l[w-1][1],x,c+1)
m,n=int(input()),int(input())
l=[]
for i in range(n):
    k=input().split()
    l.append([k[0],int(k[1])])
w,x=int(input()),input()
f(w,x,0)
