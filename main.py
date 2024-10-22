# Тестовое задание - написать программу на python 3.xx (любая 3 версия) которая выводит на экран данные необходимые
# для построения диаграммы Тьюки (Ящик с усами), оценку математического ожидания, дисперсии. 
# Запрещается использовать любые сторонние модули для расчёта значений. Так же запрещается использовать встроенные
# функции сортировки, фильтрации, поиска максимума и минимума. Результатом работы должны быть 7 чисел 
# (положение конца левого уса, левая граница ящика, медиана, правая граница ящика, конец правого уса, 
# оценка математического ожидания и оценка дисперсии).




def main():
    data = inputData()
    Sort(data)
    median = findMedian(data)
    mean = findMean(data)
    Q1, Q3 = findQ1(data), findQ3(data)
    LWhisker, RWhisker = findLeftWhisker(data, Q1, median), findRightWhisker(data, Q3, median)
    print("Левый ус:", LWhisker)
    print("Левая граница ящика:", Q1)
    print("Медиана:", median)
    print("Правая граница ящика:", Q3)
    print("Правый ус:", RWhisker)
    print("Оценка математического ожидания:", mean)
    print("Оценка дисперсии:", findVariance(data, mean))

def inputData():
    arrSize = int(input("Введите размер массива данных: "))
    arr = [int(i) for i in input().split()]
    return arr

def findMedian(arr):
    if len(arr) % 2 == 0:
        return (arr[len(arr)//2] + arr[len(arr)//2 - 1])/2
    else:
        return arr[len(arr)//2]

def findMean(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum/len(arr)

def findVariance(arr, mean):
    sum = 0
    for i in arr:
        sum += (i - mean)**2
    return (sum/(len(arr) -1)) ** 0.5

# найти левую границу диаграммы Тьюки.
def findQ1(arr):
    return arr[len(arr)//4]

def findQ3(arr):
    return arr[len(arr)*3//4]

def findLeftWhisker(arr, Height, Q1):
    for i in range(len(arr)):
        if arr[i] > (Q1 - Height * 1.5):
            return arr[i]
        
def findRightWhisker(arr, Height, Q3):
    for i in range(len(arr)):
        if arr[i] < (Q3 + Height * 1.5):
            return arr[i]

    
def Sort(a) :
    N = len(a)
    i = 0
    while i < N-1:
        j = 0
        while j < N-1-i:
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            j += 1
        i += 1


if __name__ == '__main__':
    main()