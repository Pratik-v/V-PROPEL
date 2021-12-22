#QUESTION
'''Two equal length strings S1 and S2 are said to be stepped strings if the difference between the letter position in English alphabet of non space characters is ‘i’ where ‘i’ 
is the position of the character in the strings excluding spaces in the strings. Letter position of character ‘a’ in English alphabet is 1, letter position of character ‘b’ is 
2 and so on.

 

Given two strings S1 and S2, write a C program to check if S1 and S2 are stepped strings. If the strings are of different length then print  "Length different" and if strings 
contain non alphabets then print "Strings contain non alphabets" and if strings differ in the position of space then print  "Strings differ in space" and print  "Strings are 
not stepped" when valid strings are given and they differ in the step value

 

Input Format

First line contains the string, s

Output Format

Print either Strings are stepped or Length different or Strings differ in space or Strings are not stepped or Strings contain non alphabets'''

#CODE
s1,s2=input(),input()
if(len(s1)!=len(s2)): exit(print("Length different"))
if(s1.index(" ")!=s2.index(" ")): exit(print("Strings differ in space"))
s1,s2=(s1[:s1.index(" ")]+s1[s1.index(" ")+1:]),(s2[:s2.index(" ")]+s2[s2.index(" ")+1:])
if not (s1.isalpha() and s2.isalpha()): exit(print("Strings contain non alphabets"))
for i in range(len(s1)):
    if(ord(s2[i])-ord(s1[i])!=i+1):
        exit(print("Strings are not stepped"))
print("Strings are stepped")
