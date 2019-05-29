
opcion = None

while True:
    print('Menu:')
    print('1. Suma')
    print('2. Resta')
    print('3. Salir')
    opcion = int(input('Digite opcion: '))
    if opcion == 3:
        break
    n1 = int(input('Digite primer numero: '))
    n2 = int(input('Digite segunto numero: '))
    if opcion == 1:
        print('El resultado es: ' + str(n1 + n2))
    elif opcion == 2:
        print('El resultado es: ' + str(n1 - n2))
    else:
        print("Opcion")
