#формируем последовательность псевдослучайных чисел
from random import randint
numericList = [randint(-10, 10) for p in range(0, 20)]
#можем заменить рандинт на i выведет по порядку, если число то его 20 раз

#просто для себя вывожу максимальный элемент списка
max(numericList)
print("Максимальный элемент списка: ", max(numericList))

#поиск максимального элемента и его индекса
maxElementInList1 = 0
for i in numericList:
    if i > maxElementInList1:
        maxElementInList1 = i

#счет нулей и запись количества в счетчик
zeroCounter = 0
for j in numericList:
    if j == 0:
        zeroCounter += 1

#добавление элементов в новый список по порядку, без нулей
newNumericList = []
for k in numericList:
    if k != 0:
       newNumericList.append(k)

#поиск максимума в новом списке
maxElementInList2 = 0
for q in newNumericList:
    if q > maxElementInList2:
        maxElementInList2 = q

#добавление нулей при нахождении максимума в новом списке
for x in newNumericList:
    if x == newNumericList.index(maxElementInList2):
        newNumericList.insert(maxElementInList2 + 1, 0) #вставляет один ноль, а надо чтобы все из счетчика

#надо подумать над тем что индекс не берется за начало

print("Cписок псевдослучайных чисел: ", numericList)
print("Список чисел после решения задачи: ", newNumericList)
print("Сколько нулей в списке: ", zeroCounter)
print("Индекс максимального элемента списка А: ", numericList.index(maxElementInList1))
print("Индекс максимального элемента списка B: ", newNumericList.index(maxElementInList2))

