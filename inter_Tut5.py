#Lamnbda
#which stands for an anonymous function
"""
def func(x):
    return x + 5
print(func(2))
"""

func1 = lambda x: x+5
print(func1(2))

#also useful to have function within a function

def aFunc(x):
    bFunc = lambda x: x+1
    return bFunc(x) + 5
print(aFunc(2))

func0 = lambda x,y,z = 3: x+y+z #you can also you optional parameters
print(func0(1,2))

#lets mix Map, Filter and Lambda

a = [1,2,3,4,5,6,7,8,9,10]
newList = list(map(lambda x: x-1,filter(lambda x: x%2 == 0, a)))
print(newList)
