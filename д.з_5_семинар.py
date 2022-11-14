i = 2021

while i > 0:
     a = int(input('Игрок 1 введите количество конфет '))
     if a > 28 or a < 0:
         raise ValueError('Играй по правилам')
     elif a < 29 and a > 0:
         if i - a == 0:
             print('Победил 1 игрок')
             break
         elif i - a <= 0:
             raise ValueError('Неверный ход')
         else:
             i = i - a
             print(f'Осталось {i} конфет')
     b = int(input('Игрок 2 введите количество конфет '))
     if b > 28 or b < 0:
         raise ValueError('Играй по правилам')
     elif a < 29 and a >= 0:
         if i - b == 0:
             print('Победил 2 игрок')
             break
         elif i - b <= 0:
             raise ValueError('Неверный ход')
         else:
             i = i - b
             print(f'Осталось {i} конфет')

