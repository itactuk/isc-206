


def obten_contenido(nombre_archivo: str) -> str:
    with open(nombre_archivo, 'r') as f:
        contenido = f.read()
        return contenido


contenido = obten_contenido('archivo.txt')

lista_lineas =  contenido.split('\n')

suma=0
for linea in lista_lineas[1:]:
    elementos = linea.split(',')
    if len(elementos) >= 3:
        nombre = elementos[0]
        apellido = elementos[1]
        salario = int(elementos[2])
        suma += salario
print(suma)

