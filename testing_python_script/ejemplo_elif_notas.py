# Leo la nota numerica
nota_numerica = int(input("Digita un nota númerica: "))

if nota_numerica >= 90:
    letra = 'A'
elif nota_numerica >= 80:
    letra = 'B'
elif nota_numerica >= 70:
    letra = 'C'
elif nota_numerica >= 60:
    letra = 'D'
else:
    letra = 'F'

print("Su calificación es: " + letra)
