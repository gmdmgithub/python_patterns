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
print(15*'#','string example',15*'#')