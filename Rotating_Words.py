'''After solving the previous problem, Kartik is stuck on yet another new problem given to him by his teacher.
The problem wants him to find out the number of unique words that can be formed by cyclically rotating a given string.

Cyclic rotation of a string is defined as moving the last character of the string on the first position.

Kartik can apply Cyclic rotation any number of times.

You have to help him in finding the maximum number of unique words that can be formed by applying Cyclic rotation any number of times.

Input Format:
The only line of the input contains a string S containing of lowercase characters

Output Format:
Print only one single integer denoting the number of unique words that can be formed as explained above.

Constraints:
1 <= len(s) <= 50

Example:
Input:
abcd
Output:
4
Explanation:
abcd,dabc,cdab,bcda
4 unique strings are possible

Input:
cc
Output:
1
Explanation:
Only 1 unique string is possible , 'cc''''

def fun(s,origin):
    if(s[-1]+s[:len(s)-1]!=origin):
        l.append(s)
    else:
        print(len(l))
        exit(0)
    fun(s[-1]+s[:len(s)-1],origin)
s=input()
l=[s]
fun(s,s)
