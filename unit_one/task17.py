# todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
# Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
# Цены хранятся в словаре:

def compute_bill(x):
    return sum(x.values())



prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
y = compute_bill(prices)
print(y)
