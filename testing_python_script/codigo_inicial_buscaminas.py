
def main():
    matriz = obten_matriz(4,6, '#')
    imprime_matriz(matriz)

def obten_matriz(m, n, valor_inicial=0):
    matriz = []
    for i in range(m):
        elementos = []
        for j in range(n):
            elementos.append(valor_inicial)
        matriz.append(elementos)
    return matriz

def imprime_matriz(matriz):
    y = 0
    print(' ', end='')
    for x in range(len(matriz[0])):
        print(x,end='')
    print()
    for elementos in matriz:
        y+=1
        print(y, end='')
        for cuadro in elementos:
            print(cuadro, end='')
        print()

if __name__ == '__main__':
    main()