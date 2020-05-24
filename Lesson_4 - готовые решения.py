# 1) ===========================================================================================

# 2) ===========================================================================================

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(new_list)

# 3) ===========================================================================================

my_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(my_list)

# 4) ===========================================================================================

from random import randint

my_list = [randint(10, 20) for i in range(20)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_list)
print(new_list)

# 5) ===========================================================================================

from functools import reduce

new_list = reduce(lambda a, b: a * b, [el for el in range(100, 1001) if el % 2 == 0])
print(new_list)

# 6) ===========================================================================================

from itertools import count, cycle

for el in count(100, 1):
    if el > 150:
        break
    else:
        print(el)

i = 1
for el in cycle('COH'):
    if i > 15:
        break
    print(el)
    i += 1

# 7) ===========================================================================================
