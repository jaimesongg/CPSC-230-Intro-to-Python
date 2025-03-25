class Person:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.height = ''

    def speak(self):
        print(f"Hello, my name is {person1.name}, I am {person1.age} years old and I am {person1.height} meters tall. ")

    def age_year(self):
        self.age+=1

    def __str__(self):
        return f"Hello, my name is {person1.name}, I am {person1.age} years old and I am {person1.height} meters tall. "

person1 = Person()
person1.name = "Jaime"
person1.age = 19
person1.height = 1.626
person1.speak()
    #classes