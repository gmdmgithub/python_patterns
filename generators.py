def square_numbers(nums):
    for i in nums:
        yield (i*i) #yield keyword create generators



my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)  # object of generators - not a list!
print(list(my_nums))
for my_num in my_nums:
    print(my_num)



my_nums2 = (x * x for x in [2, 3, 4, 5, 6])
print(list(my_nums2))

# for num in my_nums:
#     print(num)