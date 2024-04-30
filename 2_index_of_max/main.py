"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 4

[Example 2]
input = []
output = list can not blank
"""


class Solution:
    def __init__(self):
        self.numbers = [1]

    def find_max_index(self, numbers: list) -> int | str:
        if len(numbers) == 0:
            return 'List can not blank'
        else:
            maximum = max(numbers)
            index01 = numbers.index(maximum)
            return index01

Soln = Solution()
print (Soln.find_max_index([2,3,0,4,5,6]))
print (Soln.find_max_index([]))