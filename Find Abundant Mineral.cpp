/*Many minerals such as olivine, quartz, feldspar, mica, pyroxene and amphibole are found in rocks. It has been observed that in Madhya Pradesh, only one of the mineral occurs 
abundantly. Here the mineral that occurs in maximum number of rocks is said to be abundant. Given the details of minerals found in ‘n’ rocks write a C program to find out the 
mineral that has occured maximum number of times. Print only the representation of the mineral that has occurred maximum number of times. Each mineral is represented by one 
letter that is for example, olivine will be represented as o, quartz as q and so on. The minerals found in each rock is given as a string.

For example, given the details of minerals in four rocks as oqm, qfo, mpa and opf the representation of the mineral that has occurred abundantly is o.

Boundary Conditions

0<n<20

0<number of minerals<20

Input Format

First line contains the number of rocks, n

Next ‘n’ lines contain the details of minerals in each rock

Output Format

Print the representation of mineral that occur abundant*/

#include<iostream>
#include<string>
using namespace std;
int main() {
    int n;
    cin>>n;
    string m[n];
    string s="";
    for(int i=0;i<n;i++) {
        cin>>m[i];
        s+=m[i];
    }
    string ss="";
    for(int i=0;i<s.length();i++) {
        int flag=0;
        for(int j=0;j<ss.length();j++) {
            if(s[i]==ss[j]) {
                flag=1;
                break;
            }
        }
        if(flag==0)
            ss+=s[i];
    }
    int k=0,max=-1;
    for(int i=0;i<ss.length();i++) {
        int cnt=0;
        for(int j=0;j<n;j++) {
            for(int jj=0;jj<m[j].length();jj++) {
                if(ss[i]==m[j][jj]) {
                    cnt++;
                    break;
                }
            }
        }
        if(max<cnt) {
            max=cnt;
            k=i;
        }
    }
    cout<<ss[k];
}
