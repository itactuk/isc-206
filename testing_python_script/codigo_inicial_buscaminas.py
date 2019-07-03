import random


def main():
    matriz_visual = obten_matriz(6,6, '#')
    matriz_minas = obten_matriz(6,6, '0')
    colocar_minas(matriz_minas, 3)
    imprime_matriz(matriz_visual)

def obten_matriz(m, n, valor_inicial=0):
    matriz = []
    for i in range(m):
        elementos = []
        for j in range(n):
            elementos.append(valor_inicial)
        matriz.append(elementos)
    return matriz

def colocar_minas(matriz, cantidad):
    while cantidad>0:
        x = random.randint(0, len(matriz)-1)
        y = random.randint(0, len(matriz[0])-1)
        if matriz[x][y] != '*':
            matriz[x][y] = '*'
            cantidad-=1


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