## check if the list has unique values
def check_unique_list(my_list):
    return len(my_list) == len(set(my_list))


list1 = [1, 3, 2, 4, 5, 3]
list2 = [3, 5, 7, 8, 9]

print(
    check_unique_list(list1), check_unique_list(list2),
    check_unique_list('abcda'))

### check if two strings are anagram
from collections import Counter


def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)


print(Counter('My name is Alex'))
print(is_anagram('My name is', 'Alex is the best'))
print(is_anagram('a2ds', 'sa2d'))

#### byte size
import sys


def byte_size(some_str):
    return len(some_str.encode('utf-8'))


check_size = 'Hi there!'
print(f'Size {check_size}', sys.getsizeof(check_size))
print(f'Byte size {check_size}', byte_size(check_size))

### chunk the list into "n" chunks
#
from math import ceil

def chunk_list(lst, chunk_size):
    return map(lambda x: lst[x * chunk_size:x * check_size + check_size],
               list( range(0, ceil( len(lst) / check_size) ) )
               )


# print(chunk_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))

#flaten X dimensional list into one dimensional
def spread(values):
    ret_val = []
    for i in values:
        if isinstance(i, list):
            ret_val.extend(i)
        else:
            ret_val.append(i)
    
    return ret_val
def do_flatten(my_list):
    result = []

    result.extend(
        spread(list(
            map(lambda x:do_flatten(x) if type(x) == list else x, my_list)
        ))
    )

    return result

print('flatten the list',do_flatten([1,[3,4],[[5,6],9]]))


def most_frequent(my_list):
    return max(set(my_list), key=my_list.count)

my_list = [1,2,3,4,3,2,5,3,5]

print(my_list.count)

print(most_frequent(my_list))