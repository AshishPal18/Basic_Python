is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")

elif is_cold:
    print("It's a cold day")
    print("Wear warm cloths")

else:
    print("It's a lovely day")  


price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")        