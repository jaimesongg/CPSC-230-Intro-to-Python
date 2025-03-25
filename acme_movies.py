age = int(input("Please enter your age: "))
if age < 11:
    parent = input("Do you have a parent with you?\nPlease enter yes or no: ")
    if parent == 'no':
        print("Sorry, we cannot sell you any tickets. Goodbye.")
    elif parent == 'yes':
        numtick = int(input("How many ticktes would you like? "))
        studentcost = numtick * 11.50
        print("Your total cost with the student discount is: $", studentcost)
else: 
    numtickets = int(input('How many tickets would you like? '))
    adultcost = numtickets * 13.00
    print ("Your total cost is: $", adultcost)