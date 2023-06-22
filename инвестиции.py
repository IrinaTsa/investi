inv=int(input('минимальная сумма инвестиций -'))
Mike=int(input('у Майкла - '))
Ivan=int(input('у Ивана - '))
if (Mike>=inv)and (Ivan>=inv):
    print(2)
elif (Mike>=inv) or (Ivan>=inv):
    print(1)
else:
    print(0)
