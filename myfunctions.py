#Function 1
def answer(celsius):
    farenheit = 32+(celsius*1.8)
    return farenheit
print("the temperature in farenheit is: ", answer(7))
print("the temperature in farenheit is: ", answer(11))

# #Function 2
def answer(farenheit):
    celsius = ((farenheit-32)*5/9)
    return celsius
print("the temperature in celsius is: ", answer(7))
print("the temperature in celsius is: ", answer(11))

#Function 3
def palChecker(s):
    if s== s [::-1]:
        return True
    else:
        return False
print (palChecker("kayak"))

