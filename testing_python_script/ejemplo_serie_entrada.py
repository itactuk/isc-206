entrada =  input("Entre serie: ")

entero = ""
lista = []

for c in entrada:
    if c == ',':
        lista.append(int(entero))
        entero = ""
    else:
        entero += c
lista.append(int(entero))

for e in lista:
    print(e)