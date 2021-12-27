# estudos-logica
estudando logica de programação

print("------------------------\nDEPARTAMENTO DE TRANSITO\n------------------------")
a = input("em que ano estamos (yyyy): ")
b = input("em que ano você nasceu (yyyy): ")
c = int(a) - int(b)

if c >= 18:
    print("--------STATUS--------\nIDADE:",c,"\ESTÁ APTO A RETIRAR A CARTEIRA\n-----------------------------")
else:
    print("--------STATUS--------\nIDADE:",c,"\nESTÁ INAPTO A RETIRAR A CARTEIRA\n-----------------------------")
