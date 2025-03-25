price = float(input('What is the cost of a mango?'))
while price >= 0:
    Sales_Tax = float(input('What is your sales tax as a percent?'))
    
    if Sales_Tax < 0: 
        print('Eter a valid sales tax.')

    else:
        tax = (price * Sales_Tax/100)
        Final_price = (tax + price)
        print('Your final price with tax is:','$', round(Final_price,2))

Price = float(input('What is the cost of a mango?'))
