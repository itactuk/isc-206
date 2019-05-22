
acc = 0
for i in range(5):
    nota = int(input('Digite nota examen ' + str(i+1) + ' :' ))
    acc += nota
print('El promedio es: ' + str(acc/5))
