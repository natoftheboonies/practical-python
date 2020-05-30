# mortgage.py
#
# Exercise 1.7

principal = 5e5
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month=60
extra_payment_end_month=108
extra_payment = 1000

while principal > 0.01:
	month += 1
	principal = principal*(1+rate/12)
	if payment > principal:
		payment = principal
	principal = principal - payment
	total_paid = total_paid + payment
	if month >= extra_payment_start_month and month <= extra_payment_end_month:
		principal = principal - extra_payment
		total_paid = total_paid + extra_payment
	print(f'{month:>3d} {total_paid:>10.2f} {principal:10.2f}')
	

print(f'Total paid ${total_paid:0.2f}')
print(f'Months {month}')
