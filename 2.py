# 2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import math

string1 = '3/4'
string2 = '1/8'

# сплитуем дроби
string1 = string1.split('/')
string2 = string2.split('/')

# функция суммирует дроби
def sum(string1, string2):
    print('наименьший общий знаменатель найден math.gcd (fractions не работает): ', \
    math.gcd(int(string1[1]), int(string2[1])))

    # приводим к общему знаменателю
    common_divider = int(string1[1]) * int(string2[1])
    print('общий знаменатель', common_divider)
    string1_new = str(int(string1[0]) * int(string2[1])) + '/' + str(int(string1[1]) * int(string2[1]))
    string2_new = str(int(string2[0]) * int(string1[1])) + '/' + str(int(string2[1]) * int(string1[1]))
    string1_new = string1_new.split('/')
    string2_new = string2_new.split('/')

    # складываем числители  и получаем сумму дробей
    sum_tmp = str(int(string1_new[0]) + int(string2_new[0])) + '/' + str(common_divider)
    print('сумма = ', sum_tmp)

    # пробуем сократить дробь
    reduce_sum(sum_tmp)

# функция сокращает дробь
def reduce_sum(sum_tmp):
    sum_tmp = sum_tmp.split('/')
    check1 = 0
    check2 = 0
    for i in range(int(sum_tmp[1]) if int(sum_tmp[1]) > int(sum_tmp[0]) else int(sum_tmp[0]), 2, -1):
        check1 = int(sum_tmp[0]) % i
        check2 = int(sum_tmp[1]) % i
        if (check1 == 0) and (check2 == 0):
            result = str(int(sum_tmp[0]) / i) + '/' + str(int(sum_tmp[1]) / i)
            print('результат: ', result)

# функция вычисляет произведение дробей
def mult(string1, string2):
    result = str(int(string1[0]) * int(string2[0])) + '/' + str(int(string1[1]) * int(string2[1]))
    print('произведение: ', result)

sum(string1, string2)
mult(string1,string2)