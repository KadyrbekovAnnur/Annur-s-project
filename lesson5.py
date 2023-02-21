def factorial_num(num):
    part_factorial = 1
    sum_num = 0
    for number in range(1, num + 1):
        part_factorial *= number
        sum_num += part_factorial
    return sum_num
n = int(input('Введите число: '))
print(factorial_num(n))
