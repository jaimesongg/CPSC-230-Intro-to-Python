price = int(input("Enter the price: "))
if price < 0:
#if the price is a value less than zero a while loop is used for the user to enter a value greater than zero
    while price < 0:
        price = int(input("Enter a valid price greater than 0: "))
#Until the user enters a positive integer the while loop will continuously tell the user to enter avalid price
salestax = float (input("Enter the sales tax %: "))
if salestax < 0:
#if the sales tax is a value less than zero a while loop is used for the user to enter a value greater than zero
    while salestax < 0:
        salestax = int(input("Enter a valid sales tax greater than 0: "))
#until the user enters a positive integer the while loop will continuously tell the user to enter a valid sales tax
totalPrice = (price *(salestax/100.0)) + price
print("Total price with sales tax: $",totalPrice)