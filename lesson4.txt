number = int(input('Введите число: '))
sum_num = 0
while number != 0:
    last_num = number % 10
    sum_num += last_num
    if last_num == 5:
        print('Обнаружен разрыв')
        break
    number //= 10
    print('Текущая сумма цифр числа:', sum_num)
print('\nИтоговая сумма цифр числа:', sum_num)
print('I love')