def my_gen():
    n = 1
    print('This is printed first')

    # Generator function contains yield statements
    yield n

    n += 1
    print("This is printed second")
    yield n

    n += 1
    print('This is printed at last')
    yield n


for number in my_gen():
    print(number)

generator = my_gen()
# print(next(generator))
# print(next(generator))
# print(next(generator))

"""
EX2: Create a generator that does the same thing as
class MyRangeClass implemented in the EX1 exercise.
"""


def my_range(start, end):
    # start 1
    # end 4
    current = start  # 1 2 3 4
    while current < end:  # 1 < 4, 2 < 4, 3 < 4, 4 < 4
        yield current  # 1 2 3
        current += 1  # 2 3 4


# for number in MyRangeClass(1, 4):
#     print(number)

for number in my_range(1, 4):
    print(number)

# 1
# 2
# 3
