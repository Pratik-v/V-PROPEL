'''An ant has its nest in a tree which is at the bottom of a mountain. The mountain is irregular in structure that to travel from one point in the mountain to the other 
point in the mountain one has to climb up, move straight and climb down. Everyday this ant get down the tree, searches for food in the mountain and brings back the food 
to the nest. Ant moves with different speeds while it climbs down the tree, climbs up the tree, climbs down the mountain, climbs up the mountain and move straight on the 
mountain surface. Let P be the point in the mountain where food for the ant is available on a particular day.

Given the height of the tree, the distances to climb up, climb down and move straight to reach the point P from the nest of the ant and the different speeds with which 
the ant can move, determine the time taken by the ant to gather food from point P and save it in its nest. All the distances given in the problem are in meters and the 
speed of ant is given in meters/min. After calculation, ceil the time taken to next minute. Ceil function gives the next integer for all decimal places that is ceil(3.1) = 4 
and ceil(3.9) = 4.

For example, if the height of the tree is 230 meters, to reach point P from the bottom tree the ant has to climb up 170 meters, move straight by 310 meters, climb down 
217 meters and the ant can climb down the tree with speed 8 m/min, climb up the mountain with speed 6 m/min, move straight on mountain surface with speed 11m/min, climb 
down the mountain with speed 12 m/min and the ant can climb up the tree with speed 7m/min then the time taken by the ant to bring food to nest will be 3 hours and 35 minutes.

In python, ceil function for a variable ‘x’ may be used as

import math

math.ceil(x)

Input Format

First line contains the height of the tree, h

Next line contains the distance to climb up to reach point P

Next line contains the distance to move straight to reach point P

Next line contains the distance to climb down to reach point P

Next line contains the speed of the ant by which it can climb up the mountain

Next line contains the speed of the ant by which it can climb down the mountain

Next line contains the speed of the ant by which it can move straight on the mountain surface

Next line contains the speed of the ant by which it can climb up the tree

Next line contains the speed of the ant by which it can climb down the tree

Output Format

Print the number of hours and minutes (ceil to the next minute and separated by a space) taken by the ant to gather food from point P and bring back to the nest'''

import math
h=int(input())
dc=int(input())
ds=int(input())
dd=int(input())
scm=int(input())
sdm=int(input())
ssm=int(input())
sct=int(input())
sdt=int(input())
f=math.ceil((h/sdt)+(dc/scm)+(ds/ssm)+(dd/sdm)+(dd/scm)+(ds/ssm)+(dc/sdm)+(h/sct))
print(f//60,f%60)
