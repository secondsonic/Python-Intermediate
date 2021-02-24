#collections Deque(deck)

import collections
from collections import deque

##d = deque('String')
##d.appendleft(1)
##d.append('s')
##
##d.popleft()
##d.pop()
##
##d.clear()
##
##d.extend('456')
##d.extend('hello')
##d.extend([1,2,3])
##d.extendleft('hey')
##
##d.rotate(-1)
##d.rotate(2)

d = deque('Hello', maxlen=5)
print(d)
d.append(0)
print(d)
d.extend([1,2,3])
print(d)
d.reverse()
print(d)
