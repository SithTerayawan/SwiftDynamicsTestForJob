"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    def __init__(self):
        self.number = 1

    def number_to_thai(self, number: int) -> str:
        thaiWordDict = {
            '0': 'ศูนย์',
            '1': 'หนึ่ง',
            '2': 'สอง',
            '3': 'สาม',
            '4': 'สี่',
            '5': 'ห้า',
            '6': 'หก',
            '7': 'เจ็ด',
            '8': 'แปด',
            '9': 'เก้า'
        }
        thaiIndexDict = {
            '0': 'สิบล้าน',
            '1': 'ล้าน',
            '2': 'แสน',
            '3': 'หมื่น',
            '4': 'พัน',
            '5': 'ร้อย',
            '6': 'สิบ',
            '7': '',
        }
        if number < 0:
            return 'Number can not less than 0'
        elif number == 0:
            return 'ศูนย์'
        s_num = str(number)
        while len(s_num) <= 7:
            s_num = '0' + s_num
        s_lst = [x for x in s_num]
        thaiWord = ''
        count01 = 0
        one = False
        for i in s_lst:
            if count01 == 6 and i != '0':
                one = True
            if i == '0':
                count01 += 1
                continue
            elif count01 == 6 and i == '2':
                thaiWord += 'ยี่สิบ'
            elif count01 == 6 and i == '1':
                thaiWord += 'สิบ'
            elif count01 == 7 and i == '1' and one:
                thaiWord += 'เอ็ด'
            else:
                thaiWord += thaiWordDict[i]
                thaiWord += thaiIndexDict[str(count01)]
            count01 += 1
        return thaiWord

Soln = Solution()
print (Soln.number_to_thai(8793015))
print (Soln.number_to_thai(0))
print (Soln.number_to_thai(2351))
print (Soln.number_to_thai(21))






