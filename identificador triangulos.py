

L1 = input("escreva o primeiro lado do triangulo: ")
L2 = input("escreva o segundo lado do triangulo: ")
L3 = input("escreva o terceiro lado do triangulo:")

if (int(L3)-int(L2) < int(L1) < int(L2) + int(L3)) and (int(L2) - int(L1) < int(L3) < int(L1) + int(L2)) and (int(L1)-int(L3) < int(L2) < int(L1) + int(L3)):
    print('pode ser um triangulo')
else:
    print('não pode ser um triangulo')
    quit()


    

if L1 == L2 and L2 == L3:
    print("Equilatero")
else:
    print('não é equilatero')
if L1 != L2 and L2 != L3 and L1 != L3:
    print("é escaleno")
else:
    print("não é escaleno")