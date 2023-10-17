import random

def is_valid(n):
    if (1 <= n <= 100):
        return True
    else:
        return False

count = 0
while True:
    n = random.randint(1,100)
    if is_valid(n) == True:
        print('Добро пожаловать в числовую угадайку')
        n = int(n)
        while True:
            m = int(input())
            if (m < n):
                print("Ваше число меньше загаданного")
            elif (m > n):
                print('Ваше число больше загаданного')
            else:
                print("Вы угадали! Поздравляю!")
                print("Спасибо, что играли в числовую угадайку. Ещё увидимся...")
                break
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
    