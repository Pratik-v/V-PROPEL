'''A number ‘n’ in a list at index ‘i’ (human indexing) is said to be a factor indexed number if ‘i’ is a factor ‘n’. Given two lists of numbers l1 and l2 form a list l3 by 
inserting factor indexed numbers of l1 and l2. Intialize index to ‘0’ visit elements of l1 and l2 at index, if one of them is factored indexed insert and increment index and 
go till end of the list. If both of them are factor indexed then insert element of l1 at index and then element of l2 at index and increment index. If end of one of the list 
is reached then add elements of other list to l3 if they are factor indexed. After construction of l3, Print the numbers which continues to be factor indexed in l3.

For example, if l1 contains 15, 12, 17, 32, 26, 42 and l2 contains 45, 34, 64, 80 then l3 will be 15, 45, 12, 34, 32, 80, 42 then print 15, 12, 42.

Input Format

First line contains the number of elements in l1, n1

Next ‘n1’ lines contain the elements of l1

Next line contains the number of elements in l2, n2

Next ‘n2’ lines contain the elements of l2

Output Format

Print good numbers of l3 one number in a line'''

n1=int(input())
l1=[int(input()) for i in range(n1)]
n2=int(input())
l2=[int(input()) for i in range(n2)]
l3=[]
i=1
while(l1!=[] or l2!=[]):
    if(l1!=[]):
        l11=l1.pop(0)
        if(l11%(i)==0):
            l3.append(l11)
    if(l2!=[]):
        l22=l2.pop(0)
        if(l22%(i)==0):
            l3.append(l22)
    i+=1
for i in range(1,len(l3)+1):
    if(l3[i-1]%i==0):
        print(l3[i-1])
