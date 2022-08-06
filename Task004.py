# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# x^2 + 5*x - 3
from random import randint
k = 2
with open('text.txt', 'w', encoding='utf-8') as file:
    a = randint(-10, 10)
    file.write(f'{a}*x^{k} + ')
    a = randint(-10, 10)
    file.write(f'{a}*x ')
    a = randint(-10, 10)
    file.write(f'+ {a} = 0')
