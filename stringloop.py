incrementa = 0
incremente = 0
incrementi = 0
incremento = 0
incrementu = 0


string = input('enter a string')
for eachchar in string:
    if eachchar == 'a':
        incrementa += 1
    elif eachchar == 'e':
        incremente += 1
    elif eachchar == 'i':
        incrementi += 1
    elif eachchar == 'o':
        incremento += 1
        
print('letter count a', incrementa)
print('letter count e', incremente)
print('letter count i', incrementi)
print('letter count o', incremento)
print('letter count u', incrementu)