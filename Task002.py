# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_nimbers(n):
   i = 2
   prime_nimber = []
   while i * i <= n:
       while n % i == 0:
           prime_nimber.append(i)
           n = n // i
       i = i + 1
   if n > 1:
       prime_nimber.append(n)
   return prime_nimber

n = 66
print(f'Простые множители числа {n} равны: {prime_nimbers(n)}')
