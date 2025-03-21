
class Parent:

     def greet(self):
        return "Hello from Parent"


# Inherited Parent class in Child class
class Child(Parent):
    def greet(self):
        return super().greet()+" Hello from child"


c = Child()
print(c.greet())






