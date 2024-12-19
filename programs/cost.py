price = int(input("Enter the cost price of bike:"))

if price <= 50000:
    tax = 0.05 * price
elif price <= 100000:
    tax = 0.10 * price
else:
    tax = 0.15 * price

print(tax)