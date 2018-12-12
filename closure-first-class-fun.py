import logging

logging.basicConfig(filename='example.log', level=logging.INFO)


print('################# closuer main example ##########')
def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x+y
    
def sub(x, y):
    return x-y

add_logger = logger(add) #first class function
sub_logger = logger(sub)

add_logger(3, 3) 
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)


print('################# closuer simple explanation- ##########')
#simpler explenation
def outer_func():
    message = 'Hi from outer'

    def iner_fun():
        print(message) #free variable

    return iner_fun()

outer_func() # simpler because function is returnig with result "()" means we execute the function

print('################# now just returnig function - not value ##########')
#now just returnig function - not value
def outer_func2(add_message):
    message = f'Hi from outer func 2 with passed message: {add_message}'

    def iner_fun2():
        print(message) #free variable

    return iner_fun2

my_func = outer_func2('something strange')
# and surprise - clouser is inner function that remember and has access to the values even after executing
print(my_func.__name__)
my_func()

print('################# more complex ##########')
#more complex closure
def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')
    return wrap_text # this function is returned!

print_h1 = html_tag('h1')
print_h1('Test the function with h1 inside')
print_paragraphe = html_tag('P')
print_paragraphe('New paragraphe from closure')
