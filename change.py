def change():
    expense = 23.75
    money = 100
    vuelto = str(money - expense)
    position = vuelto.find(".")
    pesos = vuelto[:position]
    print(f"pesos {pesos}")
    centavos = vuelto[position + 1:]
    print(f"centavos {centavos}")
change()
