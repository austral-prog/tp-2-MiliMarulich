def change():
    expense = 23.75
    money = 100
    vuelto = money - expense 
    pesos = (vuelto)
    centavos = int((vuelto - int(vuelto)) * 100 )
    print(f"Ingresar gasto:")
    print(expense)
    print(f"Dinero recibido")
    print(money)
    print(f"\nVuelto\n")
    print(f"Pesos:")
    print(pesos)
    print(f"Centavos:")
    print(centavos)

