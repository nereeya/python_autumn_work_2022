#todo: Взлом шифра
#Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
#Попробуйте все возможные сдвиги и расшифруйте фразу.
#grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

alfavit ='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
message = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin"
itog = ''
for i in message:
    m = alfavit.find(i)
    n = m + 20
    if i in alfavit:
        itog += alfavit[n]
    else:
        itog +=i
print(itog)

#Методом подбора подошло 20 значение.