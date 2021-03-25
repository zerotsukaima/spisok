#формируем последовательность псевдослучайных чисел
from random import randint
numericList = [randint(-10, 10) for p in range(0, 20)]
#можем заменить рандинт на i выведет по порядку, если число то его 20 раз

#вывожу максимальный элемент списка
max(numericList)
print("Максимальный элемент списка: ", max(numericList))

#поиск максимального элемента и его индекса
maxElementInList1 = 0
for i in numericList:
    if i > maxElementInList1:
        maxElementInList1 = i
maxIndex = numericList.index(maxElementInList1)

#счет нулей и запись количества в счетчик
zeroCounter = 0
for j in numericList:
    if j == 0:
        zeroCounter += 1

#добавление элементов в новый список по порядку, без нулей
newNumericList = []
for k in range(0, maxIndex + 1):
    if numericList[k] != 0:
        newNumericList.append(numericList[k])
for m in range(zeroCounter):
    newNumericList.append(0)
for r in range(maxIndex + 1, len(numericList)):
    if r != 0:
        newNumericList.append(numericList[r])

print("Cписок псевдослучайных чисел: ", numericList)
print("Список чисел после решения задачи: ", newNumericList)
print("Сколько нулей в списке: ", zeroCounter)
print("Индекс максимального элемента списка А: ", numericList.index(maxElementInList1))