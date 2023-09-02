# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
n = 1
payment_first_year = 3684.11

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

# # Extra payment of $1000 per month in first 12 months
# for n in range(1, 13):
#     principal = principal * (1 + rate/12) - payment_first_year
#     total_paid = total_paid + payment_first_year
#     print ( "Fisrst year: " ,n , round(total_paid, 2), round(principal, 2))
#     n = n + 1

while principal > 0 and principal > payment:
    if n >= extra_payment_start_month and n <= extra_payment_end_month:
        principal = principal * (1 + rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment
        print ( n , round(total_paid, 2), round(principal, 2))
    else:
        principal = principal * (1 + rate/12) - payment
        total_paid = total_paid + payment
        print ( n , round(total_paid, 2), round(principal, 2))
    n = n + 1

last_payment = principal
print(n, 'Last payment', round(last_payment,2))
total_paid = total_paid + last_payment

print('Total paid', round(total_paid,2))
print('Months', n)