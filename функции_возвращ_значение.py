# объявление функции
def merge(list1, list2):
    for i in range(len(list2)):
        list1.append(list2[i])
    list1.sort()
    return list1

print(merge([1, 2, 3], [5, 6, 7, 8]))
print(merge([1, 7, 10, 16], [5, 6, 13, 20]))