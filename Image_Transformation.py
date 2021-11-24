'''There was a spacing problem in the first test case. Now it is corrected. Apologies for that

Digital images are represented as a matrix and each element in the matrix represents the RGB value of a pixel. Given the pixel values of a nXn image. 
Write a code to transform the image into another image by alternate swap of edge pixels. That is for example, given a 4 X 4 image as follows:

1 2 3 4

5 6 7 8

9 10 11 12

13 14 15 16

The edge elements of the above image are 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9 and 5. The following steps are involved in the transformation:

1 and 3 are swapped

1 and 8 are swapped

1 and 16 are swapped

1 and 14 are swapped

1 and 9 are swapped

After doing alternate swap of edge elements the pixel values of the image looks as follows:

3 2 8 4

5 6 7 16

1 10 11 12

13 9 15 14

And given an image of dimension 5 X 5 as follows:

2 4 5 6 3

3 11 12 7 9

7 15 13 8 1

2 21 25 13 14

17 10 16 19 3

Should transform as:

5 4 3 6 1

3 11 12 7 9

2 15 13 8 3

2 21 25 13 14

7 10 17 19 16

Input Format

First line contains the dimension of the matrix, n

Next nxn lines contain the elements of the matrix in row major order. That is the elements in the first row are given followed by second row and so on

Output Format

Print the transformed nxn matrix in ‘n’ lines

Each line contains the elements of a row separated by a tab.

Note: There is a tab at the end of each line'''

n=int(input())
l=[[int(input()) for i in range(n)]for i in range(n)]
k=[]
for j in range(n-1):
    if(j%2==0):
        k.append(l[0][j])
for i in range(n-1):
    if((i+(n-1))%2==0):
        k.append(l[i][n-1])
for j in range(n-1,0,-1):
    if(((n-1)+j)%2==0):
        k.append(l[n-1][j])
for i in range(n-1,0,-1):
    if(i%2==0):
        k.append(l[i][0])
k.append(k.pop(0))
for j in range(n-1):
    if(j%2==0):
        l[0][j]=k.pop(0)
for i in range(n-1):
    if((i+(n-1))%2==0):
        l[i][n-1]=k.pop(0)
for j in range(n-1,0,-1):
    if(((n-1)+j)%2==0):
        l[n-1][j]=k.pop(0)
for i in range(n-1,0,-1):
    if(i%2==0):
        l[i][0]=k.pop(0)
for i in l:
    print(*i,sep='\t',end='\t\n')
