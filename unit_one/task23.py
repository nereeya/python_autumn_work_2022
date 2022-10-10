#todo: Взлом шифра
#Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
#Попробуйте все возможные сдвиги и расшифруйте фразу.
#grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

alfavit ='zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbaazyxwvutsrqponmlkjihgfedcba'
message = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
itog = ''
for x in range(1, 30):
    for i in message:
        m = alfavit.find(i)
        n = m + x
        if i in alfavit:
            itog += alfavit[n]
        else:
            itog +=i
print(itog.split("."))

#Методом подбора подошло 6 значение.
#"although that way may not be obvious at first unless you're dutch"


