class Dog():
    
    hisOwner = 'Aaron Vela'
    
    def __init__(self, name, age, gender):
        print('new dog added')
        self.name = name
        self.age = age
        self.gender = gender
        

dog1 = Dog('Poppy', 4, True)
dog2 = Dog('Hyla', 1, False)

print(dog1.hisOwner)