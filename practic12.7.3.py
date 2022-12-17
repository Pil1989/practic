per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=[]
bank= ['ТКБ', 'СКБ', 'ВТБ', 'СБЕР']
money = int(input("Введите сумму депозита:"))
for value in per_cent.values():
   profit = int(money / 100 * value)
   deposit.append(profit)
deposit_bank=dict(zip(bank,deposit))
print("Суммы, которые вы можете заработать:", deposit_bank)
print("Максимальная сумма, которую вы можете заработать -", max(deposit))