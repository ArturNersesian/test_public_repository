
d = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print("Список банков", "||".join(d.keys()))
list_percent = d.values()
max_percent = max(list_percent)

deposit = input("Введите сумму, которую планируете положить под проценты: ")
print("Максимальный банковский процент:", str(max_percent))
deposit_max = float(deposit)*(1+max_percent/100)
print ("Максимальная сумма, которую вы можете заработать за год:", str(deposit_max))




