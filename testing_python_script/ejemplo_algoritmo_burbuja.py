from typing import List

def main():
    mi_listado = [1, 8, 3, 4, 5]
    print(ordernar(mi_listado))

def ordernar(lista: List[int]):
    n = len(lista)
    for x in range(n):
        for i in range(n-1):
            j = i+1
            if lista[i] > lista[j]:
                tmp = lista[i]
                lista[i]=lista[j]
                lista[j]=tmp
    return lista

if __name__ == '__main__':
    main()