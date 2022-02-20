/*When a number ‘n’ is shown in a magic mirror it displays two numbers ‘n1’ and ‘n2’ in it. The number n1 is formed by the digits in odd position in n but in reverse and 
the number n1 is formed by the digits in even position in n but in reverse. For example, if the number 75346 the first number displayed in the mirror is 637 and the second 
number displayed in the mirror 45.

Input Format

First line contains the number n

Output Format

First line contains the number n1

Next line contains the number n2*/

#include<iostream>
using namespace std;
int main() {
    int n;
    string n1="",n2="";
    cin>>n;
    string s=to_string(n);
    for(int i=s.length()-1;i>=0;i--) {
        if(i%2==0)
            n1+=s[i];
        else
            n2+=s[i];
    }
    cout<<n1<<'\n'<<n2;
}
