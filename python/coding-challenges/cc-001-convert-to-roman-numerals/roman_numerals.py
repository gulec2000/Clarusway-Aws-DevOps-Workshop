print('This program converts decimal numbers to Roman Numerals')
# num = input('Please enter a number :')

# for num in range(1, 4000):
#    if num>3999 and num<1:
#        print('Not Valid Input !!!')
#    else:
#        print('This is right')
#    break

class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(py_solution().int_to_Roman(69))
print(py_solution().int_to_Roman(1649))