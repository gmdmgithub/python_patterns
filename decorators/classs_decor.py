class DecoratedClass(object):
    def __init__(self,original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call class before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratedClass
def display():
    print('display function ran ...')

@DecoratedClass
def display_param(name,age):
    print(f'My name is {name} and I am {age} years old')


display()

display_param('Greg',31)