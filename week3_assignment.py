def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount if it's 20% or more."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        discounted_price = price - discount_amount
        return discounted_price
    else:
        return price


# Loop until a valid numeric price is entered
while True:
    try:
        marked_price = float(input("Enter the initial price: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value for the price.")

# Loop until a valid numeric discount is entered
while True:
    try:
        discount_percent = float(input("Enter the percentage discount: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value for the discount.")


# Calculate the final price
final_price = calculate_discount(marked_price, discount_percent)

# Display the result with formatting
if discount_percent >= 20:
    # Use :.2f to format the price to two decimal places
    print(
        f"You are eligible for a {discount_percent}% discount, the final price is ${final_price:.2f}"
    )
else:
    print(
        f"You have not qualified for any discount today. Kindly pay ${marked_price:.2f}"
    )
