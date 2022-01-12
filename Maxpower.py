'''A new operation called maxpower, among two real numbers x , y, denoted by ***, is defined as follows.

x***y = z, where y^z =x.

x***y is the power to which a number y must be raised in order to get x.

100***10 = 2 , since 10 ^ 2 = 100.

2***10 = 0.3010, since 10 ^0.3010 = 1.99 = 2 (approximately), when rounded-off to the nearest integer,

10***2= 3.3219 since 2^3.3219 = 9.99=10 (approximately), when rounded-off to the nearest integer.

64***4 =3, since 4^3=64.

1.44 ***1.2 = 2, since 1.2^2= 1.44

Given two real numbers x and y, write a code to print the value of x***y with two decimal places only.

Boundary Conditions

x, y >= 0

Input format:

The first line is the number x.

The second line is the number y

Output format

Value of the x***y with two decimal places only'''

import math as m
x,y=int(input()),int(input())
print(format(m.log(x)/m.log(y),"0.2f"))
