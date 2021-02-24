#Collection namedtuple()

import collections
from collections import namedtuple

Point = namedtuple('point','x y z') #it separte or breaks them by space
Point0 = namedtuple('point',['x' ,'y' ,'z'])
Point1 = namedtuple('point',{'x':0 ,'y':0 ,'z':0}) #it only takes the key names

newP = Point(3,4,5)
newP0 = Point0(1,2,3)
newP1 = Point1(3,6,9)

print(newP)
print(newP0)
print(newP1)

print(newP1[0],newP1[1],newP1[2]) #same as regular tuple
print(newP1.x,newP1.y,newP1.z) #accessing by names rather than position
print(newP1._asdict()) #in form of dict
print(newP1._fields) #if you forgot the fields names

newP1 = newP1._replace(y=7)
print(newP1)

p2 = Point1._make(['a','b','c'])
print(p2)
