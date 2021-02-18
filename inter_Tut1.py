#Optional Parameters

def func(x = 1): #now by default the x already has a value
    return x ** 2

calling_func0 = func(5)  #but you can give it another value if needed
print(calling_func0)

calling_func = func()
print(calling_func)

def repeat(word, add = 5, freq = 1):
    print(word * (freq + add))

calling_repeat0 = repeat("Arsalan ")
calling_repeat = repeat("Tim", 0)


class car(object):
    def __init__(self, make, model, year, condition = 'New', kms = 0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll): #you can also have showAll default equal to True 
        if showAll:
            print("This car is a %s %s from %s, it is %s and has %s kms"
                  %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This car is a %s %s from %s."
                  %(self.make, self.model, self.year))

whip = car('Ford', 'Fusion', 2021)
whip.display(True)
false_case = car('Chevy', 'Impala', 1967)
false_case.display(False)
