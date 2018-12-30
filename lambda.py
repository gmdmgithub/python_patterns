full_name = lambda fn,ln : fn.strip().title() + " "+ln.strip().title()

print(full_name(' greg    ',' doe'))

names = ['Leon M Dove', 'kris Menson', 'John Doe']
print(names)

key = lambda name: name.split(" ")[-1].lower()

for name in names:
    print(key(name))

print(sorted(names, key=lambda name: name.split(" ")[-1].lower()))

student_tuples = [
    ('zohn', 'A', 15),
    ('Cane', 'C', 12),
    ('dave', 'B', 10)
]
sorted_stud = sorted(student_tuples, key=lambda student: student[2]) # by age
print(sorted_stud)
sorted_stud = sorted(student_tuples, key=lambda student: student[0].lower())  # by name
print(sorted_stud)
sorted_stud = sorted(student_tuples, key=lambda student: student[1].lower())  # by grade
print(sorted_stud)


def quadratic_func(a,b,c):
    """"Returns the function f(x)= a*x*x +b*x +c"""
    return lambda x: a*x**2+b*x+c

f=quadratic_func(2,-4,2)
print(f(2))

print(quadratic_func(1,3,5)(3))

################## filter and lambda ##########################
print(20*'#','filter and lambda',20*'#')
num_list = [2,3,4,5,67,43,23,12,34,56]
print('original number list',num_list)
even_num = filter(lambda x: x%2==0,num_list)
print('even from list',list(even_num))

################## map and lambda ##########################
print(20*'#','map and lambda',20*'#')
triple_list = map(lambda n:n*3,num_list)
print('tripled list',list(triple_list))

################## reduce and lambda ##########################
from functools import reduce
print(20 * '#', 'reduce and lambda', 20 * '#')
reduced_list_sum = reduce(lambda x,y:x+y,num_list, -20)#initial valu is -20
print('sum with reduce - initial value -20',reduced_list_sum)