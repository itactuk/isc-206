
x = int(input('Cantidad de numeros: '))

for i in range(1, x + 1):
    v = int(input("n"+ str(i)+": "))
    if v%3 == 0:
        print("Es divisible")
    else:
        print("No es divisible")
