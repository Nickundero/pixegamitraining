# EXERCISE: WHAT DATATYPES TO USE
# ecommerce app
# ITEMNAME - String
# QUANTITY - Integer
# PRICE - Float
# IN STOCK - Boolean

# a = Itemname
# b = Quantity
# c = Price
# d = In Stock

#SELECTION
selection = "milk"

#item 1 = eggs
egg_name = "Eggs"
egg_count = 54
egg_price_usd = 2.63
egg_stock = True
if egg_stock == True :
    egg_stock_final = "In stock"
if egg_stock == False:
    egg_stock_final = "Out of stock"

egg_status = (f"{egg_name} {egg_count}, {egg_stock_final} at ${egg_price_usd}/ea")


#item 2 - milk
milk_name = "Milk"
milk_count = 3
milk_price_usd = 4.32
milk_stock = True
if milk_stock == True :
    milk_stock_final = "In stock"
if milk_stock == False:
    milk_stock_final = "Out of stock"

milk_status = (f"{milk_name} {milk_count}, {milk_stock_final} at ${milk_price_usd}/ea")

if selection == "egg":
    print(egg_status)
elif selection == "milk":
    print(milk_status)
else:
    print("no fuckin idea what you're lookin for mate")