# List of product prices

def apply_discount(prices):
    prices_copy = prices.copy()        # use the local argument, not the global list
    for i in range(len(prices_copy)):
        if prices_copy[i] > 2.00:
            prices_copy[i] *= 0.9
    return prices_copy

# now it’s safe to call:
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]
updated_prices = apply_discount(product_prices)
print(f"Updated product prices: {updated_prices}")
