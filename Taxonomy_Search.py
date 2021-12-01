'''In linguistics, hyponym and hypernym are a type-of relationship taxonomy among the words or phrases based on their meaning. A word ‘W2’ is said to be hyponym of another 
word ‘W1’ if the meaning of ‘W2’ is included within ‘W1’. If ‘W2’ is hyponym of ‘W1’ then ‘W1’ is said to be hypernym of ‘W2’.

For example, cabbage and spinach are hyponym of greens, peas and beans are hyponyms of pulses, carrots and turnips are hyponym of roots, and potatoes and yams are hyponyms 
of tubers. Greens, pulses, roots and tubers are inturn hyponyms of vegetables. The taxonomy can be viewed in the following url.

https://tinyurl.com/yd7se5pv

In the above taxonomy, vegetables is at level 0, greens, pulses, roots and tubers are at level 1 and cabbage, spinach, peas, beans, carrots, turnips, potatoes and yam are at 
level 2.

Another example taxonomy can be seen at url:

https://tinyurl.com/y88ywkbb

Level 0 – Color

Level 1 – Purple, Red, Blue, Green

Level 2 of Purple – Crimson, Violet, Lavender

Given ‘n’ taxonomies of maximum level as 2, a name ‘p’ at level 0, a name ‘l1’ at level 1 and a name ‘c’ level 2 check p, l1 and c are at proper level of the same taxonomy.

Input Format

First line contains the number of taxonomies, n

Next few lines contains details of each taxonomy in the following order

Name of the element in the level 1 of the taxonomy

Next line contains some number of elements in level 1 of the taxonomy separated by a space

Next few lines contains the details of elements in level2 of the taxonomy separated by a space, the first string here is the name of the element in level1 and remain strings 
are the children of the element in level1

If no element is present at level2 for an element in level1 then None is given

Next line contains the name of the element to be checked at level 0, p

Next line contains the name of the element to be checked at level 1, l1

Next line contains the name of the element to be checked at level 2, l2

Output Format

Print Taxonomy present if elements p,l1 and c belong to the same taxonomy at appropriate levels and Taxonomy not present otherwise

Illustration of Input

The vegetable taxonomy is represented as follows:

vegetables

greens pulses roots tubers

pulses peas beans

roots carrots turnips

greens cabbage spinach

tubers potatoes yams

Color taxonomy is represented as:

color

purple red blue green

purple crimson violet lavender

None

None

None'''

n=int(input())
L0,L1,L2=[],[],[]
for i in range(n):
    L0.append(input())
    L11=input().split()
    L1.append(L11)
    L2.append([input().split() for i in range(len(L11))])
p,l1,l2=input(),input(),input()
if(p in L0):
    i=L0.index(p)
    if(l1 in L1[i]):
        j=L1[i].index(l1)
        if(l2 in L2[i][j]):
            exit(print("Taxonomy present"))
print("Taxonomy not present")

