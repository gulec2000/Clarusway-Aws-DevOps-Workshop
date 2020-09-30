from flask import Flask, render_template, request

app = Flask(__name__)
def convert(decimal_num):
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
           50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    num_to_roman = ''
    for i in roman.keys():
        num_to_roman += roman[i]*(decimal_num//i)
        decimal_num %= i
    return num_to_roman
print(convert(3900))
#def convert_to_roman(num):
#    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
#    sayi = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#    romanvalue = ""
#    for i, d in enumerate(sayi):
#        while (num >= d):
#            num -= d 
#            romanvalue += roman[i]
#    return romanvalue
#print(convert_to_roman(4500))
#
#def convert(num):
#    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
#    number_roman = ''
#    i = 0
#    while  num > 0:
#        for _ in range(num // val[i]):
#            number_roman += syb[i]
#            num -= val[i]
#        i += 1
#    return (number_roman)
#print(convert(3999))

@app.route('/', methods = ['GET'])
def main_get():
    return render_template('index.html', developer_name = 'Serdar', not_valid=False)

@app.route('/', methods = ['POST'])
def main_post():
    alpha = request.form['number']
    if not alpha.isdecimal():
        return render_template('index.html', developer_name = 'Serdar', not_valid = True)

    number = int(alpha)
    if not 0 < number < 4000:
        return render_template('index.html', developer_name = 'Serdar', not_valid = True)

    return render_template('result.html', number_decimal = number, number_roman = convert(number), developer_name = 'Serdar' )

if __name__=='__main__':
    app.run(debug=True)


