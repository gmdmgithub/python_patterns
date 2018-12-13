#combination - group something when order is not a matter
#permutation - group something when order is a matter

import itertools #lib for combinations and permutations

my_list = [1,2,3]

combinations = itertools.combinations(my_list, 2)
print('Combination - order does not matter')
for c in combinations:
    print(c)

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