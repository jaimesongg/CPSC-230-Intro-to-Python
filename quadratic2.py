a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

import math
x = -abs(b)
z = 2*a
y = ((b**2)-(4*a*c))
if y < 0:
#if the disciminant (y) is less than zero it will enter a while loop in which it will tell the user to enter valid numbers until the disciminant is positive
    while y < 0:
        ask = print("Discriminant is negative")
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = int(input("Enter the value of c: "))
        y = ((b**2)-(4*a*c))
        if y > 0:
        #if the discriminant (y) is greater than zero the loop will break and the equation is continued and the answer is printed
            break
    
equation1 = (x+(y**0.5))/z
equation2 = (x+(y**0.5))/z
#the full quadratic equation for both plus or minus

print("Answer 1: ", equation1)
print("Answer 2: ", equation2)

