"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:
    def __init__(self):
        self.number = 1

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return 'Number can not be negative'
        elif number == 0:
            fact = 1
        else:
            fact = 1
            for i in range(1, number+1):
                fact *= i
        count01 = 0
        while True:
            if fact % 10 == 0:
                count01 +=1
                fact /= 10
            else:
                break
        return count01


Soln = Solution()
print (Soln.find_tailing_zeroes(-1))
print (Soln.find_tailing_zeroes(7))
print (Soln.find_tailing_zeroes(20))
