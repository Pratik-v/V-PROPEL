'''In a fun game, every letter in English alphabet has a partner. The first thirteen letters of the English alphabet are called pre-partners and the next thirteen letters are called post-partners. That is ‘a’ is the pre-partner and the corressponding post-partner is ‘n’, ‘b’ is the pre-partner and the corressponding post partner is ‘o’ ....‘m’ is the pre-partner and ‘z’ is the post-partner.

In this game, players will be asked to take a lot with a string ‘w’ and they are said to won the game if the following conditions are satisfied by the letters in ‘w’:

(i) The string may be mixed with pre-partners and post-partners but all pre-partners should have a post-partner

(ii) A pre-partner should come before it’s corressponding post-partner

(iii) For a pre-partner that is in position ‘i’ it’s post-partner

(a) Shall come immediately at posititon ‘i+1’

                                                      or

(b) Should come before all corressponding post-partners of pre-partners that is in positions < i and after all corressponding post-partners of pre-partners that is in position > i.

And the player has lost the game otherwise.

For example, if the word in the lot taken is ‘abon’ then the player has won the game. All pre-partners come before the post-partner and condition (iii) is also satisfied as follows:

1) ‘o’ comes immediately after its pre-partner ‘b’, and as per condition (a) of (iii) it is acceptable

2) ‘n’ comes after its prepartner ‘a’ and it comes after the post-partners of pre-partners that has come after ‘a’ and as per condition (b) of (iii) it is acceptable

Whereas if the word in the lot taken is ‘abno’ then the player has lost the game as the post-partener ‘n’ for pre-partner ‘a’ has come before the post-partner of the pre-partner ‘b’, violates condition (iii).

And if the word in the lot is ‘aerfsbon’ then also the player has won the game as shown in the following table:

Input Format

First line contains the word, w

Output Format

Print either Won or Lost'''

def fun(w,n):
    if(w==""):
        exit(print("Won"))
    if(n<=0):
        exit(print("Lost"))
    w1=w
    for i in range(len(w)-1):
        if(ord(w[i+1])-ord(w[i])==13):
            w1=w.replace(w[i],"")
            w1=w1.replace(w[i+1],"")
    fun(w1,n-1)
w=input()
fun(w,len(w))
