#todo: Даны переменные A, B, C. Написать код который меняет местами переменные таким образом
# чтобы значения в переменных были расположены по возрастанию
# Пример 1:
A = 10
B = 3
C = 7
# Итоговый результат должен быть:
# A = 3
# B = 7
# C = 10
if A > B > C:
    print("С =", C, "В =", B, "А =", A)
if A > C > B:
    print("В =", B, "С =", C, "А =", A)
if B > A > C:
    print("С =", C, "А =", A, "В =", B)
if B > C > A:
    print("А =", A, "С =", C, "В =", B)
if C > A > B:
    print("В =", B, "А =", A, "С =", C)
if C > B > A:
    print("А =", A, "В =", B, "С =", C)
# Пример 2:
#A = 2
#B = 10
#C = 7
# Итоговый результат должен быть:
#А = 2
#B = 7
#C = 10

 

