

## check if the list has unique values
def check_unique_list(my_list):
    return len(my_list) == len(set(my_list))

list1 = [1,3,2,4,5,3]
list2 = [3,5,7,8,9]

print(check_unique_list(list1),check_unique_list(list2), check_unique_list('abcda'))


### check if two strings are anagram
from collections import Counter
def is_anagram(str1,str2):
    return Counter(str1) == Counter(str2)

print(Counter('My name is Alex'))
print(is_anagram('My name is','Alex is the best'))
print(is_anagram('a2ds','sa2d'))

#### byte size
import sys
def byte_size(some_str):
    return len(some_str.encode('utf-8'))

check_size = 'Hi there!'
print(f'Size {check_size}',sys.getsizeof(check_size))
print(f'Byte size {check_size}',byte_size(check_size))