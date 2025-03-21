#lambda
#small anonymous function no name
#can have multiple argument
#return in single line
x=10
y=20

def add(x,y):
    return x + y


add1 = lambda x, y: x+y

num = [1,2,3,4,5]

squared_numb = map(lambda x:x*2,num)
print(list(squared_numb))


even_num = filter(lambda x :x % 2 == 0,num)
print(list(even_num))
