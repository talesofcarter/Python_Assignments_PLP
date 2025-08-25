def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = float((discount_percent / 100) * price)
        discounted_price = float(price - discount_amount)
        return discounted_price
    else:
        return price

# prompt the user to enter the initial price and percentage discount
marked_price = float(input("Enter the initial price: "))
discount_percent = float(input("Enter the percentage discount: "))

final_price = calculate_discount(marked_price, discount_percent)

if discount_percent >= 20:
    print(
        f"You are eligible for a {discount_percent}% discount, the final price is {final_price}"
    )
else:
    print(f"You have not qualified for any discount today. Kindly pay {marked_price}")
