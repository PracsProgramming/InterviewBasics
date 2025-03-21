
class Parent:

    def __init__(self):
        print("Parent Constructor")

    def greet(self):
        return "Hello from Parent"


# Inherited Parent class in Child class
class Child(Parent):

    def __init__(self, title):
        super().__init__()
        self.title = title
        print(title)


    def greet(self):
        return super().greet()+" Hello from child"


c = Child('Prachi')
print(c.greet())






