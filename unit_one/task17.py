#todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
#Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
#Цены хранятся в словаре:
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
compute_bill = sum(prices.values())
print(compute_bill)
