# Написать игру "Поле чудес"

# Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
# words = ["оператор", "конструкция", "объект"]
# desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
# Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
# Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
# в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
# либо победы.
#
# Пример вывода:
#
# "Это слово обозначает наименьшую автономную часть языка программирования"
#
# ▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒
#
# Введите букву: O
#
# O  ▒  ▒  ▒  ▒  ▒  O  ▒
#
#
# Введите букву: Я
#
# Нет такой буквы.
# У вас осталось 9 попыток !
# Введите букву:

import random
att = random.randint(0,2)

words = ["оператор", "конструкция", "объект"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования", "следование, ветвление и цикл - это ...", "Некоторая сущность в цифровом пространстве, обладающая определённым состоянием и поведением, имеющая определенные свойства и операции над ними"]

otg = []
gen_x = 0
i = 0
time = 10
x = 0
k = 0
fp = 0
slovo = words[att]

while gen_x in range(len(slovo)):
    otg.append("X")
    gen_x = gen_x + 1

print("Внимание, вопрос!")
print(desc_[att])
print(otg)
print("В этом слове ", len(otg), " букв")

while otg.count("X") > 0 and time > 0:
    if otg.count("X") > 0:

        x = str(input("Назовите букву "))
        if slovo.count(x) > 1:
            p = [i for i, ltr in enumerate(slovo) if ltr == slovo[slovo.index(x)]]
            while fp < len(p):
                otg[p[fp]] = x
                fp = fp + 1
            print("Вы угадали букву!")
            print(otg)
            print("Осталось попыток: ", time)
            p = []
            fp = 0
        elif slovo.count(x) == 1:
            print("Есть такая буква!")
            otg[slovo.index(x)] = x
            print(otg)
            print("Количество оставшихся попыток: ", time)
        else:
            print("В этом слове нет такой буквы")
            time = time - 1
            print("Количество оставшихся попыток: ", time)
    else:
        print("Игра окончена!")

else:
    print("Игра окончена!")