purchase_amount = float(input("Enter your purchase amount: "))

if purchase_amount >= 1000:
    discount = 0.1 # 10% discount
elif purchase_amount >= 500:
    discount = 0.5 # 5% discount
else:
    discount= 0 # no discount

final_price = purchase_amount * (1 - discount)
print("Final price after discount: $" + str(final_price))