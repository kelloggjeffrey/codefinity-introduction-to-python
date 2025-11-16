seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

# 1: Overstock risk only if seasonal AND stock above threshold
overstock_risk = seasonal and current_stock > high_stock_threshold

# 2: Discount eligible if NOT selling well and NOT already on sale
discount_eligible = not selling_well and not on_sale

# 3: Decide to make a discount if either condition is True
make_discount = overstock_risk or discount_eligible

print("Should the item be discounted?", make_discount)