item = input("Enter what item you would like to buy: ")
if item == 'cigarettes':
    age = int(input("How old are you?"))
    if age >= 18:
        print ("Thank you for your purchase!")
    else:
        print ("Sorry I can't sell you that.")
elif item == 'alcohol':
    age = int(input("How old are you?"))
    if age >= 21:
        print ("Thank you for your purchase!")
    else:
        print ("Sorry I can't sell you that.")
else:
    print ("Thank you for your purchase")

