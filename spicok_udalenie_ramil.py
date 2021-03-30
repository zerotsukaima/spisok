from random import randint

max = 10
min = max
negative = 0
list = [randint(-10, max) for i in range(20)]
print('\nДо удаления отрицательных элементов, '
      'идущих вслед за минимальным элементом списка.: \n'
      + str(list) + '\n')
#находит минимальный элемент и его индекс
for i in range(len(list)):
    if list[i] < min:
        min = list[i]
min_in = list.index(min)

#считаем после минимального отрицательные и меняем на x
for i in range(len(list)):
    if i > min_in and list[i] < 0:
        list[i] = 'X'
        negative += 1
#удалил все х
for i in range(negative):
    list.remove('X')
print('Минимальный элемент списка: ', min)
print('\nПосле удаления отрицательных элементов,'
      'идущих вслед за минимальным элементом списка.: \n'
      + str(list))