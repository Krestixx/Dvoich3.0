print(
    'Привет! Я калькулятор переводящий десятичную систему счисления в какую либо из видов'
)
print('1: Перевод десятичной в двоичную')
print('2: Перевод десятичной в восьмиричную')
print('3: Перевод десятичной в шестнадцатиричную')

vibor = int(input('Выбор: '))


class Dvoich_calc():

    def Calc2():
        number = int(input('Введите число: '))
        binary = format(number, "b")
        print(number, '=', binary)
        print('Удачи!')

    def Calc8():
        number = int(input('Введите число: '))
        binary = format(number, "o")
        print(number, '=', binary)
        print('Удачи!')

    def Calc16():
        number = int(input('Введите число: '))
        binary = format(number, 'x')
        print(number, '=', binary)
        print('Удачи')


if vibor == 1:
    Dvoich_calc.Calc2()
if vibor == 2:
    Dvoich_calc.Calc8()
if vibor == 3:
    Dvoich_calc.Calc16()
