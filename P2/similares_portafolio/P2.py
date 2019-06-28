

entrada = ""

while True:
    entrada = input("Digite un numero o exit para salir: ")
    if entrada == "exit":
        break

    entrada = int(entrada)
    print(entrada)

for i in range(0,100):
    if i%2==1:
        continue
    print(i)