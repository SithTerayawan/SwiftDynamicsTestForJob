"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    def __init__(self):
        self.number = 1

    def number_to_roman(self, number: int) -> str:
        roman_dic = {
            '1'   : 'I',
            '5'   : 'V',
            '10'  : 'X',
            '50'  : 'L',
            '100' : 'C',
            '500' : 'D',
            '1000': 'M'
            }
        if number < 0:
            return 'number can not less than 0'
        elif number == 0:
            return '0'
        elif number > 3999:
            return 'number is more than 3999'
        s_num = str(number)
        while len(s_num) <= 3 :
            s_num = '0' + s_num
        s_lst = [x for x in s_num]

        n_lst = []
        count01 = 0
        for i in s_lst:
            if i == '0':
                count01 += 1
                continue
            elif count01 == 0:
                j = 0
                while j < int(i):
                    n_lst.append('1000')
                    j += 1
            elif count01 >= 1:
                n_ind = int(1000/(10**count01))
                if i == '9':
                    n_lst.append(str(n_ind))
                    n_lst.append(str(n_ind*10))
                elif int(i) <= 8:
                    int_i = int(i)
                    if int_i >= 5:
                        n_lst.append(str(n_ind*5))
                        int_i -= 5
                    while 0 < int_i:
                        n_lst.append(str(n_ind))
                        int_i -= 1
            count01 += 1
        romanNumber = ''
        for i in n_lst:
            romanNumber += roman_dic[i]
        return romanNumber

Soln = Solution()
print (Soln.number_to_roman(3682))
print (Soln.number_to_roman(4000))        
print (Soln.number_to_roman(89))        
        
        
        
