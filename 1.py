# 1. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('num : '))
system_number = 16
def integer_to_other_system(num, system_number):
    result = ''
    while num > 1:
        res = num % system_number
        result += str(hex(res) if res > 9 else res)
        num = num // system_number
    print(result[::-1])
    return
integer_to_other_system(num, system_number)
print('проверка -', hex(num))
