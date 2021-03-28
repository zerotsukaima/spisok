#формируем последовательность псевдослучайных чисел
from random import randint
numericList = [randint(-10, 10) for p in range(0, 20)]
print(numericList)
#можем заменить рандинт на i выведет по порядку, если число то его 20 раз

#вывожу максимальный элемент списка
min(numericList)
print("Минимальный элемент списка: ", min(numericList))

#поиск максимального элемента и его индекса
minElementInList1 = 11
for i in numericList:
    if i < minElementInList1:
        minElementInList1 = i
minIndex = numericList.index(minElementInList1)

print("Индекс минимального элемента списка: ", minIndex)
print("Cписок псевдослучайных чисел: ", numericList)