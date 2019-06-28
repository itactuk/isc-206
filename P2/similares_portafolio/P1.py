from typing import List


def producto(lista: List[int]):
    acc = 1
    for x in lista:
        acc *= x
    return acc