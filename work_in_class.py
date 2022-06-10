class Dog():
    
    hisOwner = 'Aaron Vela'
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def getDogName(self):
        print('my name is ' + self.name)
        

dog1 = Dog('Poppy', 4, True)
dog2 = Dog('Hyla', 1, False)


#dog1.getDogName()
#dog2.getDogName()

class Cat():
    
    def __init__(self, age=0):
        self.age = age
        self.humanAge = age * 7
        
cat1 = Cat(5)

print(cat1.age)
print(cat1.humanAge)