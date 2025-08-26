def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Only applies the discount if it is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Step 2: Get user input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount)

    # Print result
    if final_price < original_price:
        print(f"Discount applied. Final price: Ksh {final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: Ksh {original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values only.")
