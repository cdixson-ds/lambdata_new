
class Person():

    def __init__(self, first, birth):   
        self.first = first
        #self.last = last 
        self.birth = birth

    @property
    def get_name(self):                 
        return (self.first)

    @property
    def get_birth(self):
        return self.get_birth

class Student(Person):
    def __init__(self, first, birth, major):  
        self.major = major
        super().__init__(first, birth)

    @property
    def getMajor(self):
        return self.major

jack = Student('Jack', 1990, 'Art')

print(jack.first)
print(jack.birth)
print(jack.major)
