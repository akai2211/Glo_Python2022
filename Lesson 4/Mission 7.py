num = 1
# Не могу вспомнить как правильно сделать без этой переменной None не помог((
while num:
    num = int(input("Введите число: "))
    if 99 < num < 1000000001:
        l_nums = num % 1000
        f = l_nums % 10
        s = l_nums % 100 // 10
        t = l_nums // 100
        print('У числа', num, 'сумма последних трех цифр равна', f + s + t)
        break
    else:
        print("Введите число меньше трёх значного или больше миллиарда.")
