#Collections , Counter()

import  collections
from collections import Counter

#containers: list, set, dict, tuples(immutable)

#collection types: counter, deque, namedTuple, ordedDict, defaultdict

#a = Counter('gallad')
#print(a)
#b = Counter(['a','a','b','c','c'])
#print(b)
#c = Counter({'a':1, "b":2})
#print(c)
#d = Counter(cats = 2, dogs = 3)
#print(d['cats'])
#print(d['pet']) #you can add keys easily compare to dictoranry, and receive value 
#print(d)
#
#
#print(list(d.elements()))
#print(b.most_common(2))

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a','b','b','c'])
##c.subtract(d)
##print(c)
##c.update(d)
##print(c)
##
##c.clear()
##print(c)

print(c + d)
print(c - d)
print(c & d) #intersection
print(c | d) #union
