class Person:

    def __init__(self,name,age):
        self.name =name
        self.age =age

    def greet(self):
        return f"Hello my name is {self.name} and my age is {self.age} "


person1 = Person("abc",30)
print(person1.greet())