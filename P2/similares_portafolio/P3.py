
# Contar cantidad de cada una de las vocales en un string
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

texto = input("Digite un string")

contadores = {}

for l in texto:
    if l not in vocales:
        continue
    if l not in contadores:
        contadores[l]=0
    contadores[l] += 1

print(contadores)

