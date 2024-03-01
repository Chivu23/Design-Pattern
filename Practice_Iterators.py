lst = ['x', 'y', 'z']

for letter in lst:
    print(letter)

"""
=>  3 iterations
iteration 1 -> letter = 'x'
iteration 2 -> letter = 'y'
iteration 3 -> letter = 'z'

ITER = object that has the method available __iter__
"""

# nums = [1, 2, 3]
# print(nums.__iter__())  # check if is iter

# nums.__iter__() <-> iter(nums)
# method __iter__  return an iter object.

nums = [1, 2, 3]
i_nums = iter(nums)
# i_nums.__iter__() <-> iter(i_nums)
# i_nums.__next__() <-> next(i_nums)
print(i_nums)
print(iter(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
# print(next(i_nums))  # error msg -> StopIteration

"""
EX1: Implement a class that is so iterable as well as an iterator
and have the same behavior as the range function from Python.
"""
range(1, 5)  # -> 1, 2, 3, 4
range(3, 6)  # -> 3, 4, 5


# for x in range(1, 5):
#     print(x)
#
# print("============")

# for x in range(3, 6):
#     print(x)

# result wish

# for x in MyRangeClass(1, 5):
#     print(x)
#
# for x in MyRangeClass(3, 6):
#     print(x)


class MyRangeClass:

    def __init__(self, start, end):
        self.value = start    # 1
        self.end = end        # 4

    # make a iter class
    def __iter__(self):
        # return an iterator  ( __iter__ & __next__)
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current_value = self.value   # 1 2 3
        self.value += 1    # 2 3 4
        return current_value


nums = MyRangeClass(1, 10)
for num in nums:
    print(num)

for number in MyRangeClass(1, 4)
    print(number)