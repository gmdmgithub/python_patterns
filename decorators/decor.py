######################### foundation ################################
print(15*'#','fundation',15*'#')
def decor_func(funct):
    def inner_fun():
        result = funct()
        return result*3
    return inner_fun

def some_num():
    return 5

result_fun = decor_func(some_num)
print(result_fun())

#################### simple example ################################
print(15*'#','simple example',15*'#')

def decor_func_dec(funct):
    def inner_fun():
        result = funct()
        return result * 3

    return inner_fun

@decor_func_dec
def some_num_dec():
    return 16

print(some_num_dec())

#################### string example ################################
print(15*'#','string example',15*'#')
def decor_str(func):
    def inner_fun(n):
        result = func(n)
        result += ', how are you?'
        return result
    return inner_fun

@decor_str
def hello_name(name):
    return f'Hello {name}'

#res = decor_str(hello_name)
#print(res('cristine'))
print(hello_name('cristine'))

#################### string example ################################
print('################### decorator!!!! - how it works ############################')
#usually it works with inner functiuon!
from functools import wraps

def mapper(func):

    @wraps(func)  #wraps from functools replace the doc from original function - additional feature not nessessary here
    def inner_func(list_of_values):
        return [func(value) for value in list_of_values]

    return inner_func

@mapper
def camel_func(str):
    """ 
    return camelised string from python way string 
    
    Arguments: {str} - string to print put

    """
    return ''.join([st.capitalize() for st in str.split('_')])

#camel_func = mapper(camel_func) #this is the same as mapper!
# print('camel_func res: '+camel_func('test_the_camel_func'))

teams = ['manchester_united', 'bayern_munchen','ajax_amsterdam']

print(camel_func(teams))
print(camel_func.__doc__)

print('################### decorator with arguments !!!! - how it works ############################')
import random

def power_func(power=2):
    def mapper(fnc):
        def iner():
            return fnc()**power
        return iner
    return mapper


@power_func()
def random_odd_choice():
    return random.choice([1,3,5,7,9])

@power_func(3)
def random_even_choice():
    return random.choice([2,4,6,8,10])

print('random choice from odd num '+ str(random_odd_choice()))
print('random choice from even num '+ str(random_even_choice()))


print('################### decor next explanation ############################')
# def decor_function(original_function):
#     def wrapper_function():
#         return original_function()
#     return wrapper_function

# def display():
#     print('display function ran ...')

# decorated_display = decor_function(display)
# decorated_display()

print('this below is the same as above!!!! - beauty')

# def decor_function(original_function):
#     print('test)
#     message = 'Some message'
#     def wrapper_function():
#         print(message)
#         return original_function()
#     return wrapper_function

# @decor_function
# def display():
#     print('display function ran ...')

# display()

print('next beauty')

def decor_function(original_function): #add as many logic inside as you want
    def wrapper_function( *args, **kwargs):
        print('call method before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decor_function
def display():
    print('display function ran ...')

@decor_function
def display_param(name,age):
    print(f'My name is {name} and I am {age} years old')


display()

display_param('Greg',31)