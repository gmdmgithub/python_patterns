#mutable and immutable examples

#strings are immutable!
a = 'Greg'
print(f'Value {a} and memory addres {id(a)}')
a = 'Joe'
print(f'Value {a} and memory addres {id(a)}')

# lists are mutable
b = [1,2,3,4,5]
print(f'Value {b} and memory addres {id(b)}')
b[0]=9
print(f'Value {b} and memory addres {id(b)}')

####
employees = ['Corey', 'John', 'Rick', 'Steve', 'Carl', 'Adam']

output = '<ul>\n'

for employee in employees:
    output += f'\t<li>{employee}</li>\n'
    print(f'Address of output is {id(output)}')

output += '</ul>'
print(output)
print('\n')