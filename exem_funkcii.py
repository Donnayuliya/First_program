# объявление функции
def is_pangram(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    TEXT = text.lower()
    count = 0
    for i in range(len(alphabet)):
        if alphabet[i] not in TEXT:
            return False
    return True

# считываем данные
text = 'Jackdaws love my big sphinx of quartz'

# вызываем функцию
print(is_pangram(text))