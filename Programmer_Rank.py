'''A university conducts a number of programming contests in their programming portal every day. The problems given in the portal are categorized into easy, medium and hard. 
A student scores 10 points when he solves an easy problem, he gets 30 points when solves a medium level problem and he scores 50 points when he solves a hard problem. 
The university decides to give a ranking for the students based on their active performance in the contests. Students with the highest score get the first rank, the second 
highest score gets the second rank and so on. If more than one student, say ‘k’ students get the same score then all get the same rank ‘r’ and the next student or students 
get ‘r+k’ th rank. For example, when there are six students with the following details:

Name

Number of easy problems solved

Number of medium problems solved

Number of hard problems solved

Student1  

12 

8

9

Student2

11

8

11

Student3

10

7

10

Student4

13

7

8

Student5

12 

8

9

Student6

21 

6

7

Total points scored by the students are:

Student1 -  810  

Student2  -  900

Student3 - 810

Student4 - 740

Student5 - 810

Student6 - 740

Rank given for the students are as follows:

Student1 - 2  

Student2  - 1

Student3 - 2

Student4 - 5

Student5 - 2

Student6 - 5

Given the name of the student, the number of easy problems solved, the number of medium problems solved and the number of hard problems solved write a code to display the 
rank and the name of the students.

Input Format

The first line contains the number of students, n

Next ‘n’ lines contain the name, the number of easy problems solved, the number of medium problems solved, the number of hard problems solved separated by a space each.

Output Format:

Print rank of student and the name of the student separated by a space arranged in ascending order of rank. When the rank is same for more than one student print in 
ascending order of name. Print name and rank of one student in one line.

Illustration

For the example described above, input and output should be as follows:

Input

6

Student1 12 8 9

Student2 11 8 11

Student3 10 7 10

Student4 13 7 8

Student5 12 8 9

Student6 21 6 7

Output

1  Student2

2  Student1

2  Student3

2  Student5

5  Student4

5  Student6'''

n=int(input())
l=[input().split() for i in range(n)]
l2=[[i[0],(int(i[1])*10)+(int(i[2])*30)+(int(i[3])*50)] for i in l]
l2.sort(reverse=True,key=lambda x:x[1])
scores=[i[1] for i in l2]
rank=[scores.index(i)+1 for i in scores]
for i in range(len(l2)):
    print(rank[i]," ",l2[i][0])
