from decimal import Decimal
principal = Decimal('10000.00')
rate = Decimal('0.05')
for year in range(1,11):
	amount = principal * (1 + rate) ** year
	print(year,amount)
#eof
