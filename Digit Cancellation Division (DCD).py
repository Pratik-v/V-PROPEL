'''A new operation, called a Digit Cancellation Division (DCD) , represented symbolically using /// is performed among the integers. Here x///y, where x and y are integers is computed as follows.

1. Identify the common digits that occur in the integers x and y.

2. Cancel the common digits, processing from the leftmost digit to the rightmost digit. Integers with no common digits are kept as it is. If all the digits in the numerator or denominator gets canceled then replace it by multiplicative identity 1.

3. Perform normal division between the numbers after cancellation of common digits

If y is zero, then x///y is -1.

Given two integers, write a pseudocode and the subsequent code to find x///y.

For example,

When the operation 243///41 is done, after cancellation of the common digits, we will have 23//1. The common digit 4 can occur in any position. After cancellation of the digits, 3 which was in units position , is in the ten’s position.

23///74 will be as it is.

In 1///121, we have the common digit 1, which occurs once in the numerator and twice in the denominator. In that case, digits in the left will get canceled first.

1///121 = 1/21.

101///121 = 0/2;

2. After the cancellation of digits, perform the usual division (/)operation with the remaining digits in the numerator and the denominator.

Input format :

First line contains the numerator, x

Second line contains the denominator, y

Output Format:

Always print the value of x///y in the two decimal format.

Use format function to print two decimal places. 

Syntax: format(s,'0.2f'), to fromat s with two decimal places

Illustration:

Input :

49

98

Output :

0.50

Input :

231

0

Output

-1.00'''

x,y=input(),input()
for i in x:
    for j in y:
        if(i==j):
            x=x[:x.index(i)]+x[x.index(i)+1:]
            y=y[:y.index(j)]+y[y.index(i)+1:]
            break
if(x==''):
    x='1'
if(y==''):
    y=1
if(y!='0'):
    print(format(int(x)/int(y),'0.2f'))
else:
    print('-1.00')
