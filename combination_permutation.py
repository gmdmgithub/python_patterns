#combination - group something when order is not a matter
#permutation - group something when order is a matter

import itertools #lib for combinations and permutations
import random

my_list = [1,2,3]

print('########## COMBINATION ####')
combinations = itertools.combinations(my_list, 2)
print('Combination - order does not matter')
for c in combinations:
    print(c)

print('########## PERMUTATION ####')
permutations = itertools.permutations(my_list, 2)
print('Permutation - order does matter')
for p in permutations:
    print(p)

my_list = [1,2,3,4,5,6]
combinations = itertools.combinations(my_list, 3)
permutations = itertools.permutations(my_list, 3)

print([result for result in combinations if sum(result) == 10])

word = 'sample'
my_letters = 'plmeas'

combinations = itertools.combinations(my_letters, 6)
permutations = itertools.permutations(my_letters, 6)

for p in permutations:
    #for p in combinations:
    # print p
    if ''.join(p) == word:
        print('Match!')
        break
else:
    print('No Match!')


########## Radom ####
print('########## RANDOM ####')

def random_walk(n):
    """"return coordintats after n block wandom walk"""
    x,y =0,0
    for i in range(n):
        (dx, dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x +=dx
        y +=dy
    return (x,y)

for i in range(5):
    walk = random_walk(10)
    print(walk, 'Distance = ', abs(walk[0]) + abs(walk[1]))
