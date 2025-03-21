# classmethod : can be called without creating object of that method
# these method can not access instance variables i.e. self.name
class NewClass:

    @classmethod
    def clas_method(cls):
        return "class"

    def instance_method(self):
        return "Instance"


obj = NewClass()

print(obj.instance_method())
print(NewClass.clas_method())