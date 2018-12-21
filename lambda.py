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
    