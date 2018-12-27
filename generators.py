 #pip install memory_profiler

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

# t1 = time.clock()
# people = people_list(1000000) # never convert into list - you lose everything
# t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

# print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())
print('Memory (After) : ' + str(mem_profile.memory_usage()) + 'MB')

# print 'Took {} Seconds'.format(t2-t1)
print('Took ' + str(t2 - t1) + ' Seconds')