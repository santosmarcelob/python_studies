#Pure functions
# 2 rules:
#   1) given the same input it will always return the same output
#   2) A function should not produce any side effects (things that affects the 'outside world')

#map, filter, zip and reduce

##### MAP ####

# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list

# def multiply_by2(item):
#     return item*2

# print(list(map(multiply_by2, [1,2,3])))

####   FILTER    #####
# my_list = [1,2,3]

# def only_odd(item):
#     return item % 2 != 0

# print(list(filter(only_odd, my_list)))

###  ZIP  ###

# my_list = [1,2,3]
# your_list = [10,20,30]

# print(list(zip(my_list, your_list)))

