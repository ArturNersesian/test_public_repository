name = input("Как я могу к Вам обращаться? ")
tickets_quantity = int(input(f"{name},какое количество билетов Вы бы хотели приобрести? "))
listOfAge = [int(input(f"введите возраст {i+1}-го посетителя ")) for i in range(tickets_quantity)]

totalSum = 0
lowPrice = 0
midPrice = 990
fullPrice = 1390

for age in listOfAge:
    if age < 18:
        totalSum = totalSum + lowPrice
    elif age >=18 and age <= 25:
        totalSum = totalSum + midPrice
    else:
        totalSum = totalSum + fullPrice

if  tickets_quantity <= 3:
        print(f"Общая сумма всех билетов равна {totalSum} рублей")
else:
        totalSum = totalSum * 0.9
        print(f"{name}, поскольку Вы приобретаете более 3-х билетов, общая сумма всех билетов со скидкой равна {totalSum} рублей")

