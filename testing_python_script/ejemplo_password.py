
mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = mayusculas.lower()

x=input("password:")

valido = True
tiene_mayuscula = False
for lm in mayusculas:
    if lm in x:
        tiene_mayuscula = True

if not tiene_mayuscula:
    valido = False
elif not caracter_especial:
    valido = False


