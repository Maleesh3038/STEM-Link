purchase_amount = float(input("Enter your purchase amount: "))

if purchase_amount >= 100:
    discount = 20/100

elif purchase_amount >= 50:
    discount = 10/100

else: 
    discount = 0.0

discount_amount = purchase_amount * discount
final_price = purchase_amount - discount_amount

print(f"Original Price: ",purchase_amount)
print(f"Discount Amount: ",discount)
print(f"Final Price: ",final_price)