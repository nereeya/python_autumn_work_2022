#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

#Содержимое файла import_this.txt
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.

#выходные данные print(f.readlines(4), "\n",  f.readlines(3), "\n", f.readlines(2), "\n", f.readlines(1))
#Complex is better than complicated.
#Simple is better than complex.
#Explicit is better than implicit.
#Beautiful is better than ugly.

#В первом случае не получилось вывести каждый
f = open("import_this.txt", "r")
p = f.readlines()
p.reverse()
print("\n".join(p))


