#static and class methods
class person(object):

    population = 50    #class variable

    def  __init__(self, name, age, hair): #constructor method
        self.name = name
        self.age = age
        self.hair = hair

    @classmethod    #it can be called on any instance of class
    def getPopulation(cls):
        return cls.population

    @staticmethod   #similar to class but the parameter is neither class nor self
    def is_adult(age):
        return age >= 18
    def hair_color(hair):
        print("Hair color changed to", hair)

    def display(self):
        print(self.name, 'is', self.age, 'years old.', 'Hair color is', self.hair)

new_person = person('Arsalan', 20, 'Black')

print(person.getPopulation())
print(person.is_adult(20))
person.display(new_person)
person.hair_color('Blue')

