# Get the prices of the ingredients from the user for the near supermarket
near_tomatoes_price = float(input("Enter price of 1 kg tomatoes in near supermarket: "))
near_parsley_price = float(input("Enter price of 1 bunch of parsley in near supermarket: "))
near_bulgur_price = float(input("Enter price of 1 kg bulgur in near supermarket: "))
# Get the prices of the ingredients from the user for the far supermarket
far_tomatoes_price = float(input("Enter price of 1 kg tomatoes in far supermarket: "))
far_parsley_price = float(input("Enter price of 1 bunch of parsley in far supermarket: "))
far_bulgur_price = float(input("Enter price of 1 kg bulgur in far supermarket: "))

price_difference = [0, 0, 0]
# Calculate the price difference between the two supermarkets / priority to the near store
price_difference[0] = (near_tomatoes_price - far_tomatoes_price)/near_tomatoes_price
price_difference[1] = (near_parsley_price - far_parsley_price)/near_parsley_price
price_difference[2] = (near_bulgur_price - far_bulgur_price)/near_parsley_price

counter = 0
# Counting ingredients with more than 30% difference
for difference in price_difference:
    if difference >= 0.3:
        counter += 1

# Determine from which supermarket Samir should buy
if counter >= 2:
    print("Far")
else:
    print("Near")