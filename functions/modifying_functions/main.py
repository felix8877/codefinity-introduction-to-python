def apply_discount(price, discount=0.05):
    discounted_price = price*(1-discount)
    return discounted_price
def apply_tax(price, tax=0.07):
    taxed_price = price*(1+tax)
    return taxed_price
def calculate_total(price, discount=0.05, tax=0.07):
    discounted = apply_discount(price, discount)
    
    toal_price=apply_tax(discounted, tax)
    return toal_price
    
total_price_default = calculate_total(120)
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with default discount and tax: ${total_price_default}")
print(f"Total cost with custom discount and tax: ${total_price_custom}")


