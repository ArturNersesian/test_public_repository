#print("Hello World")
#print(round (3.14159**2/2))
#pi = 31.4159265
#print ("%.4e" % (pi))



d = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print("Список банков", "||".join(d.keys()))
list_percent = d.values()
max_percent = max(list_percent)
#print(list_percent)
deposit = input("Введите сумму, которую планируете положить под проценты: ")
print("Максимальный банковский процент:", str(max_percent))
deposit_max = float(deposit)*(1+max_percent/100)
#print (deposit_max)
print ("Максимальная сумма, которую вы можете заработать за год:", str(deposit_max))


#text = input("Введите текст:")
#unique = list(set(text))
#print("Количество уникальных символов: ", len(unique))


