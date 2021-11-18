'''IronMan is stuck on a level of the Infinity War game which he is playing now. To advance this level, he has to kill all the N dragons that are present on this level. 
IronMan and the dragons have strength, which is represented by an integer. In the fight between him and dragon, the fight's outcome is determined by their strength. 
Initially, IronMan's strength equals S.

If IronMan starts dueling with the ith (1 <= i <= N) dragon and IronMan's strength is not greater than the dragon's strength Xi, then IronMan loses the duel and dies. 
But if IronMan's strength is greater than the dragon's strength, then he defeats the dragon and gets a bonus strength increase by Yi.

IronMan can fight the dragons in any order. Your task is to find out if he will be able to win all the duels without any loss.

Input Format:
The first line will contain two space-separated integers, the initial strength S and the number of dragons N.
Then N lines follow, each of which contains two space-separated integers Xi and Yi, where Xi is the strength of the dragon and Yi is the bonus strength which IronMan gains 
after defeating this dragon.

Output Format:
Print a single line containing either "YES" (without quotes), if IronMan can defeat all dragons or "NO" (without quotes) if he can't.

For example:
Input:
2 2
1 99
100 0

Output:
YES

Explanation:
IronMan's initial strength is 2 and the number of dragons also equals 2
The first dragon has strength equal to 1 and thus IronMan can defeat this dragon and gain 99 points
making his strength equal to 2 + 99 = 101.
Since 101 > 100, IronMan can defeat this dragon also and thus the answer is YES.

Second example:

Input:
8 1
100 100

Output:
NO

Explanation:
IronMan's initial strength is 8 but the required strength for the first dragon is 100 and hence, he dies and we print "NO". '''

S,N=map(int,input().split())
l=sorted([list(map(int,input().split())) for i in range(N)])
for i in l:
    if(i[0]<S):
        S+=i[1]
    else:
        exit(print("NO"))
print("YES")
