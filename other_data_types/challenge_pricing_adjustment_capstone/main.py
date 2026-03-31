grocery_inventory={"Milk":("Dairy",3.50,8),"Eggs":("Dairy",5.50,30),"Bread":("Bakery",2.99,15),
                   "Apples":("Produce",1.50,50)}
price_egg = grocery_inventory.get("Eggs")[1]
if price_egg>5:    
    grocery_inventory["Eggs"]=("Dairy",price_egg-1, 30)
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of Eggs is reasonable.")
grocery_inventory.update({"Tomatoes":("Produce",1.20,30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
quantity_milk = grocery_inventory.get("Milk")[2]
if quantity_milk< 10:
    
    grocery_inventory["Milk"]=("Dairy",3.50,quantity_milk+20)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")
price_apple = grocery_inventory.get("Apples")[1]
if price_apple>2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
print("Updated inventory:", grocery_inventory)
    