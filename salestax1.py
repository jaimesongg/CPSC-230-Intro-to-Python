price = int(input("enter the price: "))
salesTax = float (input("enter the sales tax %: "))
if salesTax < 0:
        print("enter a valid sales tax > 0")
else:
        totalPrice = (price *(salesTax/100.0)) + price
        print("Total Price w/tax:$", totalPrice)