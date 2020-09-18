num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
# def num2roman(num):
num=input("Roma Rakamina cevrilecek bir sayi giriniz :")
if num=='exit':
    print('good bye')
elif type(num)== str:
    print("Not Valid Input !!!")
elif int(num)>4000 or int(num)<1:
    print("Not Valid Input !!!")
else:
    roman = ''
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
    print(roman)