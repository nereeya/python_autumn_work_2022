# todo: 7.1 Дано целое число A. Проверить истинность высказывания: «Число A является четным».
# todo: 7.2 Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
# Примечание: В задании  требуется вывести логическое значение True, если выражение
# для введеных исходных данных является истинным, и значение False в противном случае.
print("Введите значение А")
A = input()
A = int(A)
print(bool(A % 2))
#В данном случае остаток получается 0, если четное и 1 если нечетное. Тогда выводится Ложь при четных и Правда при нечетных

print("Введите значение В")
B = input()
B = int(B)
if B % 2 == 0:
    C = 1
    print(bool(C))
else:
    C = 0
    print(bool(C))

