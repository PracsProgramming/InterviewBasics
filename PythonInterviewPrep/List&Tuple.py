#list are mutable and tuple are immutable

my_list = [1,2,3]

my_list.append(4)

print(my_list)

my_list[0] = 100

print(my_list)

my_list.pop(0)
print(my_list)

my_tuple = (1,2,3)

print(my_tuple)

# my_tuple[0] = 100
#TypeError: 'tuple' object does not support item assignment

print(my_tuple)
