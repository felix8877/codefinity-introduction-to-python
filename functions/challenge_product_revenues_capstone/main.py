# 1. Initialize the lists
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

# 2. Define function to calculate revenue
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        result = prices[i] * quantities_sold[i]
        revenue.append(result)
    return revenue

# 3. Define function to sort and print output
def formatted_output(revenue_per_product):
    # Sort alphabetically by the first element in the tuple (product name)
    sorted_list = sorted(revenue_per_product)
    for name, rev in sorted_list:
        print(f"{name} has total revenue of ${rev}")

# --- Execution Flow ---

# Calculate the revenues
revenue = calculate_revenue(prices, quantities_sold)

# Combine products and revenue into a list of tuples
revenue_per_product = list(zip(products, revenue))

# Call the output function
formatted_output(revenue_per_product)

print(revenue_per_product)