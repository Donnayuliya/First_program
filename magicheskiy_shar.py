import random

answear = ["Бесспорно",
           "Предрешено",
           "Никаких сомнений",
           "Определённо да",
           "Можешь быть уверен в этом",

           "Мне кажется да",
           "Вероятнее всего",
           "Хорошие перспективы",
           "Знатоки говорят - да",
           "ДА",

           "Пока не ясно, попробуй снова",
           "Спрсоси позже",
           "Лучше не рассказывать",
           "Сейчас нельзя предсказать",
           "Сконцентрируйся и перефразируй",

           "Даже не думай",
           "Мой ответ - Нет",
           "Звёзды говорят -НЕТ",
           "Перспективы не оч",
           "Весьма сомнительно"
           ]

print("Привет мир! Я магический шар, и я знаю ответ на любой вопрос. Назови своё имя, путник")
name = input()
print("Приветик,", name)

while True:
    q = input("Задай свой вопрос ...")
    print(random.choice(answear))
    print("Хочешь ещё спросить что-то? (да/нет)")
    ans = input()
    if ans.lower() == 'да':
        continue
    else:
        print("Возвращайся, если возникнут вопросики!")
        break