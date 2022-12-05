# todo:Создайте программу, которая будет выводить все возможные комбинации при броске 2 игральных костей
# и сумму их значений. У игральной кости стороны пронумерованы от 1 до 6.

# Пример вывода:
# Сумма 2   комбинация [(1,1)]
# Сумма 3   комбинация [(1,2),(2,1)]
# Сумма 4   комбинация [(1,3),(3,1),(2,2)]
# .......................................
# Выводы комбинаций оформить в список кортежей.

# import itertools
# num = [1, 2, 3, 4, 5, 6]
# x = itertools.combinations(num, 2)
# y = itertools.combinations(num, 2)
# for i in list(x):
#     for j in list(y):
#         print("сумма:", sum(i+j), "комбинация:", i, j)

def combo(x, y):
    res = {}
    for i in x:
        for j in y:
            summ = i + j
            if summ not in res:
                res[summ] = [(i, j)]
            else:
                res[summ] = res.get(summ) + [(i, j)]
    return res


dice_1 = [1, 2, 3, 4, 5, 6]
dice_2 = [1, 2, 3, 4, 5, 6]

for key, var in combo(dice_1, dice_2).items():
    print("Сумма", key, "комбинация", var)
