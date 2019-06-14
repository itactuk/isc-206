from typing import List


def main():
    mi_listado = [1,8,3,4,5]
    print(busqueda_secuencial(mi_listado,1))

def busqueda_secuencial(lista: List[int], elemento):
    for i in range(0, len(lista)):
        if lista[i] == elemento:
            return i
    return -1

if __name__ == '__main__':
    main()