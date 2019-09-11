#pip install memory_profiler
#generators are functions that returns sequence of values - memory efficient
#yield - wydajność, uzysk - main

import memory_profiler as mem_profile
import random
import time


def square_numbers(nums):
    for i in nums:
        yield (i*i) #yield keyword create generators



my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)  # object of generators - not a list!
print(list(my_nums))
for my_num in my_nums:
    print(my_num)

#by the list comprehension - but with bracets is a generator!
my_nums2 = (x * x for x in [2, 3, 4, 5, 6])
print(my_nums2)
print(list(my_nums2))



print('################### MORE COMPLEX ###############################')

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# print('Memory (Before): {}Mb '.format(mem_profile.memory_usage_psutil()))
print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB')


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


#huge difference between Generator (yield) and list!!

# t1 = time.clock() ## - time clock is deprecated - using time_counter
# people = people_list(1000000) # never convert into list - you lose everything
# t2 = time.clock()

t1 = time.perf_counter()
people = people_generator(1000000)
t2 = time.perf_counter()

# print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())
print('Memory (After) : ' + str(mem_profile.memory_usage()) + 'MB')

# print 'Took {} Seconds'.format(t2-t1)
print('Took ' + str(t2 - t1) + ' Seconds')

print('################### NEXT EXAMPLE ###############################')
def generate_dif(num1,num2):
    while(num1<num2):
        yield num1
        num1 +=1

res = generate_dif(2,20)
for i in res:
    print(i)

#fibonacci generator

def fib_gen(num):
    a, b = 0,1
    for i in range(1,num):
            yield "Fib {} and {}".format(i,a)
            a, b = b, a+b

for fib in fib_gen(11):
    print(fib)
        