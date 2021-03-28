#формируем последовательность псевдослучайных чисел
from random import randint
numericList = [randint(-10, 10) for p in range(0, 20)]
print(numericList)
print("Минимальный элемент списка: ", min(numericList))

#поиск максимального элемента и его индекса
minElementInList1 = 11
for i in numericList:
    if i < minElementInList1:
        minElementInList1 = i
minIndex = numericList.index(minElementInList1)

newNumericList = []
for i in range(0, minIndex + 1):
    if numericList[i] < minIndex:
        newNumericList.append(numericList[i])

#for i in range(minIndex + 1, len(numericList)):
    #if i > 0:
       # newNumericList.remove(i)
    #else:
       # newNumericList.append(numericList[i])

print("Индекс минимального элемента списка: ", minIndex)
print("Cписок псевдослучайных чисел: ", numericList)