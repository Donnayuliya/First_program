a = [1, 7, -3, 9, 0, -67]
n = len(a)

for i in range(1, n):
    elem = a[i]  # первый элемент из неотсортированной части списка
    j = i
    while j >= 1 and a[j - 1] > elem:
        a[j] = a[j - 1]
        j -= 1
    a[j] = elem
    print (a)


print("Отсортированный список:", a)
