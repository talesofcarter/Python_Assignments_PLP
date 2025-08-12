def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = float((discount_percent / 100) * price)
        discounted_price = float(price - discount_amount)
        return discounted_price
    else:
        return price
    
print(calculate_discount(1250, 30)) #875
print(calculate_discount(1250, 10)) #1250
print(calculate_discount(600, 73)) #162
print(calculate_discount(100, 20)) #80
print(calculate_discount(25957, 21)) #20,506.03